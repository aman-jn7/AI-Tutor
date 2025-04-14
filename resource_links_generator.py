from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

def get_resource_chain(llm):
    resource_links_prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant who curates high-quality educational resources based on web search snippets.

        From the provided search results, carefully identify and list **5 of the most useful and beginner-friendly learning resources** for the topic. Prioritize **clarity**, **accessibility**, and **reliability**.

        Your output should follow this format:
        - **Title or Short Description**: [Direct URL]

        ✅ Prioritize links that:
        - Come from trusted platforms (e.g., Coursera, YouTube, Udemy, GeeksForGeeks, Physics Wallah .edu sites)
        - Are free to access or clearly labeled if paid
        - Include tutorials, beginner courses, videos, or step-by-step guides
        - Are likely to be valid and not broken

        🚫 Avoid:
        - Broken links, duplicate sources, or irrelevant pages
        - Overly technical or paywalled content unless clearly noted

        Make sure the list is diverse (e.g., not all from YouTube) and helpful to someone new to the topic.

        Topic: {topic}
        Web Search Snippets: {web_search}
        """
    )

    return resource_links_prompt | llm