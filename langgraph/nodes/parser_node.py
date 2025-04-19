import os
import requests
from dotenv import load_dotenv
from vector_db import query_example_vectorstore, query_doc_vectorestore


load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "appliactaion/json"
    }


def call_llm_api(prompt: str) -> str:
   
    payload = {"inputs": prompt,
               "parameters": {
                   "temperature": 0.7,
                   "max_new_tokens": 1024,
                   "return_full_text": False
               }
               }

    response = requests.post(API_URL,
                             headers=headers,
                             json=payload)
    
    result = response.json() #  преобразует JSON-ответ сервера в Python-словарь
    return result[0]['generated_text']

def parse_request(text: str) -> dict:
    examples = query_example_vectorstore(text)
    docs = query_doc_vectorestore(text)
    example_texts = "\n\n".join([
        f"""Пример: 
        Описание: {text}
        JSON: {json.dumps(sample, ensure_ascii=False, indent=2)}""" for sample in examples
    ])

    doc_context = "\n\n".join(docs)

    prompt = f"""
Ты — помощник, который превращает текстовую инструкцию в JSON-структуру для BPMN-диаграммы в стиле mermaid.js.

Вот примеры похожих описаний и их JSON-структуры:
{example_texts}

Вот выдержки из документации:
{doc_context}
Прочитай описание и верни ТОЛЬКО JSON следующего вида:

{{
    "nodes": [
        {{ "id": "A", "type": "StartEvent", "label": "Название события" }},
        {{ "id": "B", "type": "Process", "label": "Описание шага" }},
        {{ "id": "C", "type": "Decision", "label": "Выбор" }},
        {{ "id": "D", "type": "EndEvent", "label": "Результат" }}
    ],
    "edges": [
        {{ "from": "A", "to": "B", "label": "Условие (может быть пустым)", "type": "-->" }}
    ]
}}

Типы узлов (поле `"type"`):  
- "StartEvent" — начальное событие  
- "Process" — шаг процесса  
- "Decision" — точка выбора  
- "EndEvent" — финальное состояние  

Тип стрелок (`"type"`) — всегда "-->".

ВАЖНО:  
- Верни только JSON без пояснений.  
- Строго соблюдай структуру: nodes, edges, id, label, type, from, to.  
- Все ID должны быть буквами (`A`, B, C и т.д.).



Описание:  
{text}
"""
    
    response = call_llm_api(prompt)

    try:
        return eval(response) # или json.loads(responce)
    except Exception as e:
        print('Ошибка при парсинге', e)
        print("Ответ LLM:", response)
        return {}