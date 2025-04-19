from utils.search import search_documentation
from utils.vector_db import create_vector_db
from utils.extract_pdf_text import extract_text_from_pdf
from call_llm_api import call_llm_api  # твоя функция для работы с LLM API

def call_llm_api_with_documentation(prompt: str, collection: chromadb.Collection) -> str:
    # Ищем по запросу в документации
    doc_results = search_documentation(prompt, collection)

    # Формируем информацию для модели
    docs_text = "\n".join(doc_results)

    # Создаем запрос с добавлением текста из документации
    complete_prompt = f"""
Ты помощник, который использует документацию для создания BPMN-диаграмм.
Вот несколько фрагментов документации, которые могут помочь:

{docs_text}

Теперь на основе этой информации, а также на основе примеров, преобразуй текстовый запрос в JSON:

Описание: {prompt}
"""

    # Отправляем запрос модели
    response = call_llm_api(complete_prompt)
    return response