from langchain_core.prompts import ChatPromptTemplate


class PromptService:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_template(
            """
You are an Enterprise AI Assistant.

Answer ONLY from the provided context.

If the answer is not available in the context, say:

"I don't have enough information to answer that."

Context:
{context}

Question:
{question}

Answer:
"""
        )