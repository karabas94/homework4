try:
    mushroom = int(input("Введите количество грибов: "))
    if mushroom > 0:
        if 5 <= mushroom % 10 <= 9 or mushroom % 10 == 0 or 11 <= mushroom % 100 <= 14:
            m = "ов."
        elif 1 < mushroom % 10 < 5:
            m = "а."
        elif mushroom % 10 == 1:
            m = "."
    else:
        print("Маша нашла в лесу 0 грибов")
    print(f"Маша нашла в лесу {mushroom} гриб{m}")
# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")