from nodes.parser_node import parse_request

def main():
    print("Проверка работы парсера через Hugging Face API.\n")

    input_text = input("Введите описание процесса: ")

    result = parse_request(input_text)

    print("\n=== Результат JSON ===")
    print(result)

if __name__ == "__main__":
    main()
