from langchain_core.output_parsers import StrOutputParser

from src.llm.groq_service import get_llm
from src.prompts.prompt_template import PromptService


class RAGChain:

    def __init__(self):

        self.llm = get_llm()

        self.prompt = PromptService().get_prompt()

        self.parser = StrOutputParser()

        self.chain = self.prompt | self.llm | self.parser

    def invoke(self, context, question):

        return self.chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )
