#1
def range_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

a = int(input("Введіть перше число діапазону: "))
b = int(input("Введіть друге число діапазону: "))
print("Сума чисел у діапазоні:", range_sum(a, b))
print("="*50)


#2
def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

list_str = input("Введіть числа через пробіл: ")
nums2 = list(map(int, list_str.split()))
print("Добуток елементів:", product_of_list(nums2))
print("="*50)


#3
def find_min(numbers):
    return min(numbers)
print("Мінімальне число у списку:", find_min(nums2))
print("="*50)


#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    return sum(1 for num in numbers if is_prime(num))


print("Простих чисел у списку:", count_primes(nums2))
print("="*50)


#5
def remove_number(numbers, target):
    count = numbers.count(target)
    while target in numbers:
        numbers.remove(target)
    return count
target = int(input("Введіть число для видалення: "))
nums5 = nums2.copy()  # копія, щоб зберегти попередній список
removed = remove_number(nums5, target)
print("Кількість видалених елементів:", removed)
print("Список після видалення:", nums5)
print("="*50)


#6
def merge_lists(list1, list2):
    return list1 + list2

list1 = list(map(int, input("Введіть перший список через пробіл: ").split()))
list2 = list(map(int, input("Введіть другий список через пробіл: ").split()))
merged = merge_lists(list1, list2)
print("Об'єднаний список:", merged)
print("="*50)
#7
def power_list(numbers, power):
    return [num ** power for num in numbers]
exp = int(input("Введіть ступінь: "))
result = power_list(merged, exp)
print("Список після піднесення до ступеня", exp, ":", result)
print("="*50)
