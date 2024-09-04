#Попадюк Олександр
number = int(input("Введите трехзначное число: "))
sum = (number // 100) + (number // 10 % 10) + (number % 10)
print("Сумма цифр числа:", sum)