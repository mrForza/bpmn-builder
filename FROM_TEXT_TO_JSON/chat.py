from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI  # Новый импорт для OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory  # Новый импорт для истории

# Примеры + инструкция
EXAMPLES = """
Пример:
Текст: "Вот приходит клиент. Далее смотри сколько у него денег. Если больше 1000 — даем ему кредит, иначе — нет"
JSON:
{
  "nodes": [
    {"id": "A", "label": "Клиент приходит", "type": "StartEvent"},
    {"id": "B", "label": "Проверка баланса", "type": "Decision"},
    {"id": "C", "label": "Выдача кредита", "type": "Process"},
    {"id": "D", "label": "Отказ в кредите", "type": "Process"},
    {"id": "E", "label": "Конец", "type": "EndEvent"}
  ],
  "edges": [
    {"from": "A", "to": "B", "style": "-->"},
    {"from": "B", "to": "C", "condition": "больше 1000", "style": "-->"},
    {"from": "B", "to": "D", "condition": "меньше или равно 1000", "style": "-->"},
    {"from": "C", "to": "E", "style": "-->"},
    {"from": "D", "to": "E", "style": "-->"}
  ]
}
"""

INSTRUCTION = """
Ты — помощник, который превращает текстовую инструкцию в JSON-структуру BPMN-диаграммы (mermaid.js).
Возвращай только JSON.
Используй только следующие типы узлов:
- StartEvent, Process, Decision, EndEvent

Типы стрелок:
- Normal with arrow: --->
- Dotted with arrow: -.-->

{EXAMPLES}

Теперь пользователь пишет:
"{input}"
Ответь только JSON-структурой.
"""

# Инициализация FastAPI
app = FastAPI()

# Модель запроса
class Message(BaseModel):
    user_text: str

# LangChain подготовка
api_key = "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"

# Новый шаблон
prompt = PromptTemplate(
    input_variables=["input"],
    template=INSTRUCTION.replace("{EXAMPLES}", EXAMPLES)
)

# Новый импорт для OpenAI
llm = ChatOpenAI(
    openai_api_key=api_key,
    model_name="qwen/qwen-2.5-coder-32b-instruct",
    temperature=0.2
)

# Новый подход для работы с памятью и историей
memory = ConversationBufferMemory()
history = RunnableWithMessageHistory(memory=memory, history_messages_key="history")

# POST endpoint
@app.post("/chat")
async def chat_handler(msg: Message):
    # Используем новый метод для генерации ответа
    response = history.run({"input": msg.user_text})
    return {"response": response}