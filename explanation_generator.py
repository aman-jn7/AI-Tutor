from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

def get_explanation_chain(llm):
    explanation_prompt = ChatPromptTemplate.from_template(
        """
        You are a patient and engaging tutor who specializes in making complex topics easy to understand.

        Explain the following topic to a complete beginner. Use simple language, real-life examples, and analogies where helpful. Avoid technical jargon unless it's explained clearly.

        End your explanation with a quick summary or a fun fact related to the topic.

        Topic: {topic}
        """
    )

    return explanation_prompt | llm
