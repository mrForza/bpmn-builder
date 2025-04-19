import chromadb
from sentence_transformers import SentenceTransformer

# Инициализация клиента и модели для преобразования текста в эмбеддинги
client = chromadb.Client()
embedding_function = SentenceTransformer('all-MiniLM-L6-v2')

# Создание коллекции для примеров
def get_example_vectorstore():
    return client.get_or_create_collection(name="samples", embedding_function=embedding_function)

# Создание коллекции для документации
def get_doc_vectorstore():
    return client.get_or_create_collection(name="docs", embedding_function=embedding_function)

# Добавление документов в коллекцию
def add_documents_to_collection(collection, chunks, metadatas):
    collection.add(
        documents=chunks,
        metadatas=metadatas,
        embeddings=embedding_function.encode(chunks)  # Добавление эмбеддингов
    )

# Функция для получения примеров по запросу (поиск в коллекции)
def query_example_vectorstore(query_text: str, top_k=5):
    collection = get_example_vectorstore()
    results = collection.query(query_text, n_results=top_k)
    return results['documents']  # Получаем документы из результатов

# Функция для получения документов по запросу (поиск в коллекции)
def query_doc_vectorstore(query_text: str, top_k=5):
    collection = get_doc_vectorstore()
    results = collection.query(query_text, n_results=top_k)
    return results['documents']  # Получаем документы из результатов