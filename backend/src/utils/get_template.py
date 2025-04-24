def get_template(chat_history: str, examples: str, user_text: str) -> str:
    return f"""
Ты — помощник, который превращает текстовую инструкцию в JSON-структуру для BPMN-диаграммы в стиле mermaid.js.Учти историю:

История:
{chat_history}

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
{examples}

ВАЖНО:   
- Строго соблюдай структуру: nodes, edges, id, label, type, from, to.  
- Все ID должны быть буквами (A, B, C и т.д.).
- Если пользователь не просит менять типы стрелок, то оставляй их такими же какие ты использовал при первичном создании json

Текущий запрос: {user_text}
"""
