from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

def get_quiz_chain(llm):
    quiz_prompt = ChatPromptTemplate.from_template(
        """
        You are a creative quiz generator.

        Based on the explanation below, create **5 intermediate-level multiple choice questions**. Each question should test basic understanding of the topic and have **4 answer options** (labeled A-D), with only one correct answer.

        After each question, include the correct answer in this format: **Correct Answer: B**

        Make the quiz friendly and engaging for learners.

        Explanation:
        {explanation}
        """
    )

    return quiz_prompt | llm