class ContextBuilder:

    @staticmethod
    def build(documents):

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        sources = []

        for document in documents:

            source = document.metadata.get("source")

            if source and source not in sources:
                sources.append(source)

        return context, sources