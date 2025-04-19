def generate_final_json(parsed_data: dict) -> dict:
    if not parsed_data:
        return {"error": "Пустой результат от парсера"}
    
    return parsed_data