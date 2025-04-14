from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

def get_study_plan_chain(llm):
    study_plan_prompt = ChatPromptTemplate.from_template(
        """
        You are a skilled study planner.

        Based on the topic provided, generate a comprehensive study schedule tailored to a beginner. Break the learning process into logical steps or phases. For each step, include what to learn, how to learn it (e.g., watch a video, take notes, practice questions), and the estimated time needed.

        Adjust the number of steps and time required based on the topic's complexity. Suggest any free tools, platforms, or resources that would help.

        If the topic is related to coding, programming, or any programming language (e.g., Python, Java, JavaScript), then include 1–2 high-quality YouTube video links (with titles) in the relevant steps to help the user learn effectively.

        Make the schedule easy to follow, motivating, and actionable.

        Topic: {topic}
        """
    )

    return study_plan_prompt | llm