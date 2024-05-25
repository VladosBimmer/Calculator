def calculator():
    while True:
        try:
            expression = input("Введите выражение (для выхода наберите 'exit'): ")
            if expression == "exit":
                print("До свидания!")
                break
            result = eval(expression)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка ввода. Попробуйте еще раз.", e)

calculator()
