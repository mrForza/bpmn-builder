from vector_db import get_sample_vectorstore, get_doc_vectorstore
import json

# Получение похожих примеров (top-k)
def retrieve_relevant_examples(query: str, k: int = 3):
    vectorstore = get_sample_vectorstore()
    results = vectorstore.query(
        query_texts=[query],
        n_results=k
    )
    
    examples = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        try:
            example = {
                "text": meta["text"],
                "json": json.loads(meta["json"])
            }
            examples.append(example)
        except Exception as e:
            print("Ошибка парсинга примера:", e)
    return examples

# Получение документационного контекста
def retrieve_doc_context(query: str, k: int = 3):
    vectorstore = get_doc_vectorstore()
    results = vectorstore.query(
        query_texts=[query],
        n_results=k
    )
    
    chunks = results["documents"][0]
    return "\n\n".join(chunks)