from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
import chainlit as cl
from dotenv import load_dotenv
import os

from explanation_generator import get_explanation_chain
from quiz_generator import get_quiz_chain
from study_plan_generator import get_study_plan_chain
from resource_links_generator import get_resource_chain
from code_interpreter import generate_code_prompt, programming_languages
from email_reminder import send_study_plan_email

load_dotenv()

azure_endpoint = "https://models.inference.ai.azure.com"
github_token = os.getenv("GITHUB_TOKEN")
serpapi_key = os.getenv("SERPAPI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(
    temperature=0.3,
    model_name="gpt-4o-mini",
    openai_api_key=github_token,
    openai_api_base=azure_endpoint,
)

# Setup Web Search Tool using SerpAPI
search = SerpAPIWrapper(serpapi_api_key=serpapi_key)

# Chains
explanation_chain = get_explanation_chain(llm)
quiz_chain = get_quiz_chain(llm)
study_plan_chain = get_study_plan_chain(llm)
resource_links_chain = get_resource_chain(llm)

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Welcome to **AI Tutor Team**!\n\nPlease enter the topic you want to learn about, and I will generate a full study plan, explanation, quiz, and useful learning links just for you. 🧠📚\n\n**Enter a topic to get started!**"
    ).send()

@cl.on_message
async def main(message: cl.Message):

    topic = message.content.strip().lower()

    if topic in ["bye", "exit", "quit", "goodbye"]:
        await cl.Message(content="👋 Thanks for learning with AI Tutor Team! See you next time!").send()
        return

    if not topic or len(topic.split()) < 1:
        await cl.Message(content="❗ Please enter a valid topic to get started.").send()
        return
    
    # Web Search
    try:
        search_result = search.run(topic)
        top_result = search_result.split("\n")[0] if "\n" in search_result else search_result.split(".")[0] + "."
        top_result = top_result.strip("[]'\"") 
        await cl.Message(content=f"🌐 **Topic Introduction:**\n{top_result}").send()
    except Exception as e:
        await cl.Message(content=f"🌐 **Web Search Failed:** {str(e)}").send()

    # Study Plan
    plan = await study_plan_chain.ainvoke({"topic": topic})
    await cl.Message(content="📚 **Study Plan**\n" + plan.content).send()

    # Explanation
    explanation = await explanation_chain.ainvoke({"topic": topic})
    await cl.Message(content="🧠 **Topic Explanation**\n" + explanation.content).send()

    # Quiz
    quiz = await quiz_chain.ainvoke({"topic": topic, "explanation": explanation.content})
    await cl.Message(content="📝 **Quiz**\n" + quiz.content).send()

    # Learning Resources from web search via LLM
    resources = await resource_links_chain.ainvoke({"topic": topic,"web_search": search_result})

    await cl.Message(content="🔗 **Additional Learning Resources**\n" + resources.content).send()

    # Code Execution
    if topic in programming_languages:
        code_prompt = generate_code_prompt(topic)
        # Generate code using LLM
        code_example = llm.predict(code_prompt).strip()
        await cl.Message(content=f"💻 **Example Code Snippet:**\n{code_example}\n```").send()
    
    email_reply = await cl.AskUserMessage(content="📧 Would you like to receive this study plan by email? Enter your email address or type 'no'.").send()

    user_email = email_reply.get("output", "").strip().lower()

    if "@" in user_email and "." in user_email:
        sent = send_study_plan_email(to_email=user_email, topic=topic, study_plan=plan)
        if sent:
            await cl.Message(content="✅ Study plan emailed successfully!").send()
        else:
            await cl.Message(content="❌ Failed to send email. Please try again later.").send()
    elif user_email == "no":
        await cl.Message(content="📭 Okay, skipping email reminder.").send()


    # Save in session
    cl.user_session.set("quiz_questions", quiz)
    cl.user_session.set("explanation", explanation)
    cl.user_session.set("topic", topic)

@cl.on_chat_end
async def end():
    await cl.Message(content="Thanks for using AI Tutor Team! Come back anytime you want to learn something new.").send()

@cl.on_chat_resume
async def resume():
    await cl.Message(content="Welcome back! Ready to continue learning?").send()

port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    cl.run(port=port, host="0.0.0.0")