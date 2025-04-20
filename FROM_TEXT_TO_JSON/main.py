import requests


example_texts = """ [
  {
    "input": "Отрисуй мне бизнес-процесс: Вот приходит клиент. Далее смотри, сколько у него денег на счету. Если больше 1000, то даем ему кредит на машину, если меньше — то нет.",
    "output": {
      "nodes": [
        { "id": "A", "type": "StartEvent", "label": "Приходит клиент" },
        { "id": "B", "type": "Process", "label": "Проверка баланса" },
        { "id": "C", "type": "Decision", "label": "Достаточно ли средств?" },
        { "id": "D", "type": "Process", "label": "Выдача кредита" },
        { "id": "E", "type": "EndEvent", "label": "Конец" },
        { "id": "F", "type": "Process", "label": "Отказ в кредите" }
      ],
      "edges": [
        { "from": "A", "to": "B", "label": "Клиент приходит", "type": "-->" },
        { "from": "B", "to": "C", "label": "Проверка баланса", "type": "-->" },
        { "from": "C", "to": "D", "label": "Если больше 1000", "type": "-->" },
        { "from": "C", "to": "F", "label": "Если меньше 1000", "type": "-->" },
        { "from": "D", "to": "E", "label": "Выдача кредита", "type": "-->" },
        { "from": "F", "to": "E", "label": "Отказ", "type": "-->" }
      ]
    }
  },
  {
    "input": "Отрисуй процесс обработки заказа. Когда заказ поступает, проверяется наличие товара на складе. Если товар есть, происходит упаковка и отправка, если нет — заказ отменяется.",
    "output": {
      "nodes": [
        { "id": "A", "type": "StartEvent", "label": "Заказ поступил" },
        { "id": "B", "type": "Process", "label": "Проверка наличия товара" },
        { "id": "C", "type": "Decision", "label": "Товар в наличии?" },
        { "id": "D", "type": "Process", "label": "Упаковка" },
        { "id": "E", "type": "Process", "label": "Отправка" },
        { "id": "F", "type": "EndEvent", "label": "Заказ завершен" },
        { "id": "G", "type": "Process", "label": "Отмена заказа" }
      ],
      "edges": [
        { "from": "A", "to": "B", "label": "Начало", "type": "-->" },
        { "from": "B", "to": "C", "label": "Проверка", "type": "-->" },
        { "from": "C", "to": "D", "label": "Если товар есть", "type": "-->" },
        { "from": "C", "to": "G", "label": "Если нет товара", "type": "-->" },
        { "from": "D", "to": "E", "label": "Упаковка", "type": "-->" },
        { "from": "E", "to": "F", "label": "Отправка", "type": "-->" }
      ]
    }
  },
  {
    "input": "Нарисуй процесс приема звонка. Если звонок от клиента, то принимаем заказ, если нет — игнорируем.",
    "output": {
      "nodes": [
        { "id": "A", "type": "StartEvent", "label": "Получен звонок" },
        { "id": "B", "type": "Decision", "label": "Это звонок от клиента?" },
        { "id": "C", "type": "Process", "label": "Прием заказа" },
        { "id": "D", "type": "EndEvent", "label": "Завершение" }
      ],
      "edges": [
        { "from": "A", "to": "B", "label": "Звонок", "type": "-->" },
        { "from": "B", "to": "C", "label": "Если клиент", "type": "-->" },
        { "from": "B", "to": "D", "label": "Если не клиент", "type": "-->" },
        { "from": "C", "to": "D", "label": "Прием заказа", "type": "-->" }
      ]
    }
  }
]"""

def get_bpmn_json(api_key, user_text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Version": "2",  # Важно для корректной работы
    }

    # Промпт для генерации JSON
    prompt = f"""
Ты — помощник, который превращает текстовую инструкцию в JSON-структуру для BPMN-диаграммы в стиле mermaid.js.

Вот примеры типов стрелок, которые можно использовать в диаграмме:

- Normal: ---
- Normal with arrow: --->
- Thick: ==
- Thick with arrow: =>
- Dotted: -.-
- Dotted with arrow: -.-->

Также вот список возможных типов узлов и их краткое описание:

1. Card: Notched Rectangle — Represents a card
2. Collate: Hourglass — Represents a collate operation
3. Com Link: Lightning Bolt — Communication link
4. Comment: Curly Brace — Adds a comment
5. Comment Right: Curly Brace — Adds a comment
6. Comment with braces on both sides: Curly Braces — Adds a comment
7. Data Input/Output: Lean Right — Represents input or output
8. Data Input/Output: Lean Left — Represents output or input
9. Database: Cylinder — Database storage
10. Decision: Diamond — Decision-making step. Consider question or reason in label
11. Delay: Half-Rounded Rectangle — Represents a delay
12. Direct Access: Horizontal Cylinder — Direct access storage
13. Disk Storage: Lined Cylinder — Disk storage
14. Display: Curved Trapezoid — Represents a display
15. Divided Process: Divided Rectangle — Divided process shape
16. Document: Document — Represents a document
17. Event: Rounded Rectangle — Represents an event
18. Extract: Triangle — Extraction process
19. Fork/Join: Filled Rectangle — Fork or join in process flow
20. Internal Storage: Window Pane — Internal storage
21. Junction: Filled Circle — Junction point
22. Lined Document: Lined Document — Lined document
23. Lined/Shaded Process: Lined Rectangle — Lined process shape
24. Loop Limit: Trapezoidal Pentagon — Loop limit step
25. Manual File: Flipped Triangle — Manual file operation
26. Manual Input: Sloped Rectangle — Manual input step
27. Manual Operation: Trapezoid Base Top — Represents a manual task
28. Multi-Document: Stacked Document — Multiple documents
29. Multi-Process: Stacked Rectangle — Multiple processes
30. Odd: Odd — Odd shape
31. Paper Tape: Flag — Paper tape
32. Prepare Conditional: Hexagon — Preparation or condition step
33. Priority Action: Trapezoid Base Bottom — Priority action
34. Process: Rectangle — Standard process shape
35. Start: Circle — Starting point
36. Start: Small Circle — Small starting point
37. Stop: Double Circle — Represents a stop point
38. Stop: Framed Circle — Stop point
39. Stored Data: Bow Tie Rectangle — Stored data
40. Subprocess: Framed Rectangle — Subprocess
41. Summary: Crossed Circle — Summary
42. Tagged Document: Tagged Document — Tagged document
43. Tagged Process: Tagged Rectangle — Tagged process
44. Terminal Point: Stadium Text Block — Terminal point Text block

Каждый узел в диаграмме имеет "id", "type" и "label". Связи между узлами указываются через "from" и "to", а также указываются стрелки для указания типа перехода между ними.

Вот примеры похожих описаний и их JSON-структур:

{example_texts}


Типы узлов (поле "type"):  
- "StartEvent" — начальное событие, начало диаграммы/- "Process" — шаг процессы
- "Decision" — точка выбора. В графе "label" должен быть вопрос или условие. Выходов в другие вершины может быть несколько.
- "EndEvent" — финальное состояние, завершение диаграммы 

ВАЖНО:   
- Строго соблюдай структуру: nodes, edges, id, label, type, from, to.  
- Все ID должны быть буквами (A, B, C и т.д.).

Описание:  
{user_text}
"""
    data = {
        "model": "qwen/qwen-2.5-coder-32b-instruct",  # было 32B
        # "qwen/qwen2.5-coder-7b-instruct"
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1500,
        "mode": "json"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # Ответ в формате JSON
    else:
        print(f"Ошибка {response.status_code}: {response.text}")
        return None


if __name__ == "__main__":
    api_key = "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" # Вставь сюда свой ключ
    user_text = '''Приготовление блюда в ресторане начинается с того, что шеф-повар собирает команду на утреннюю
     планерку, где обсуждаются цели на день, специальные предложения и наличие продуктов на складе, и вот уже повара
      берут в руки списки, чтобы отправиться на кухню, где уже разложены свежие ингредиенты, благоухающие специи и
       инструменты, которые они любят; один из помощников повара с утра пришел, чтобы замариновать мясо, в то время 
       как другой уже нарезает овощи для салата, а третий очистает картошку на пюре, аромат из кухни становится все 
       более насыщенным, и здесь же упаковка с рыбой, решается вопрос, как лучше ее обработать, чтобы сохранить
        текстуру и вкус, ведь каждое блюдо должно радовать не только душу, но и тело, есть рулетка с приправами –
         добавлять или нет, а шеф все время наблюдает за процессом, и в один момент вносит свои коррективы, предлагая
          альтернативные варианты, вот и закипает бульон, и запах укропа наполняет пространство, повара работают 
          слаженно, как механизм, один выкладывает ингредиенты, другой следит за временем, ведь важна каждая секунда, 
          подходя ко времени подачи, они начинают ковать финальные штрихи, кто-то ставит гриль, кто-то готовит соус,
           накрывается тарелка, и, наконец, идет финальная проверка – цвет, аромат, текстура и подача, каждый элемент
            на своем месте, и тут раздается команда – подача в зал; официанты берут блюдо, оно выглядит красиво, а 
            затем передается гостю, который с нетерпением ждет первых укусов, и вместе с ним работники кухни 
            расслабляются, зная, что все прошло без сучка и задоринки, пока шеф уже планирует следующее меню,
             рассматривая новые концепции, а мечты о новых блюдах кружат в его голове, как движение ложки по кастрюле,
              удовлетворение от хорошо выполненной работы – неоценимый опыт, который заставляет продолжать стремиться
               к совершенству в каждой тарелке.'''
    response = get_bpmn_json(api_key, user_text)
    if response:
        print("Ответ от модели:")
        print(response)
