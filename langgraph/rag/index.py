import json
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def build_vector_store():
    with open("rag_data/samples.json", "r", encoding="utf-8") as f:
        samples = json.load(f)

    documents = [Document(page_content=sample["text"], metadata={"json": sample["json"]}) for sample in samples]

    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

    vectorstore = Chroma.from_documents(documents. embedding_model, persist_directory="rag_data/vectorstore")

    vectorstore.persist()
    print("Индексация завершена. Векторное хранилище создано.")

if __name__ == "__main__":
    build_vector_store()