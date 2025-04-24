import json
from typing import Any

from langchain.memory import ConversationBufferMemory
import ollama

from src.services.base import Service
from src.utils import get_examples, get_template


class BpmnGenerationConfig:
    api_key: str | None = None
    models: list[str] = ["gemma3:1b"]
    url: str = "localhost:11434"


default_config = BpmnGenerationConfig()


class BpmnGenerationService(Service):
    def __init__(self, config: BpmnGenerationConfig = default_config):
        self.config = config
        self.memory = ConversationBufferMemory(return_messages=True)

    def _generate_prompt(self, user_text: str) -> str:
        """Generate prompt for BPMN generation"""
        history = self.memory.load_memory_variables({}).get("history", [])
        chat_history = (
            "\n".join([msg.content for msg in history]) if history else "Нет истории"
        )

        return get_template(chat_history, get_examples(), user_text)

    async def generate_bpmn(
        self, user_text: str, model: str | None = None
    ) -> dict[str, Any]:
        """Generate BPMN from user text"""
        if model and model not in self.config.models:
            raise ValueError(
                f"Model: {model} not supported. Here are the supported models: {self.config.models}"
            )
        else:
            model = self.config.models[0]
        prompt = self._generate_prompt(user_text)
        client = ollama.AsyncClient(host=self.config.url)
        messages = [
            {
                "role": "system",
                "content": "Ты преобразуешь текстовые описания в BPMN JSON. Отвечай ТОЛЬКО JSON.",
            },
            {"role": "user", "content": prompt},
        ]

        response = await client.chat(
            model=model,
            messages=messages,
            format='json',
        )

        output = json.loads(response["message"]["content"])
        self.memory.save_context(
            {"input": user_text},
            {"output": json.dumps(output, indent=2, ensure_ascii=False)},
        )
        
        return output

    @property
    def history(self): ...
