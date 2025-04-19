from sentence_transformers import SentenceTransformer

def search_documentation(query: str, collection: chromadb.Collection) -> list:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Преобразуем запрос в вектор
    query_embedding = model.encode([query])

    # Ищем в базе данных
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3  # Количество результатов
    )

    return results['documents']