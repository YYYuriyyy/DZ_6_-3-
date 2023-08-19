##  № 1
# #Вивести на екран усі прості числа в діапазоні, зазначеному користувачем.
# #Число називається простим, якщо воно ділиться без залишку тільки на себе та на одиницю

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Введіть початкове число діапазону: "))
end = int(input("Введіть кінцеве число діапазону: "))

print("Прості числа в діапазоні: ")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)

##  № 2
#Вивести на екран таблицю множення для всіх чисел від 1 до 10

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j} = {i*j}", end=" ")
    print()

##  № 3
# #Вивести на екран таблицю множення в діапазоні, зазначеному користувачем.
# #Наприклад, якщо користувач вказав 3 і 5

number = int(input("Введіть перше число: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

number1 = int(input("Введіть друге число: "))
for i in range(1, 11):
    result = number1 * i
    print(f"{number1} * {i} = {result}")

