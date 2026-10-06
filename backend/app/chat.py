from rag_pipeline import RAGPipeline

pipeline = RAGPipeline()

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    response = pipeline.ask(question)

    print("\nAnswer\n")

    print(response["answer"])

    print("\nSources\n")

    for source, page in response["sources"]:

        print(f"{source} - Page {page}")