def print_quote():
    print('"Don\'t compare yourself with anyone in this world…')
    print('    if you do so, you are insulting yourself."')
    print('        Bill Gates')
print_quote()

def print_even_numbers(start, end):
    print(f"Парні числа між {start} та {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=' ')
    print()
print_even_numbers(3, 17)

def print_square(size, symbol, filled):
    for i in range(size):
        if filled or i == 0 or i == size - 1:
            print(symbol * size)
        else:
            print(symbol + ' ' * (size - 2) + symbol)
print("Порожній квадрат:")
print_square(5, '#', False)
print("Заповнений квадрат:")
print_square(5, '*', True)

def min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)
print("Мінімальне з 5 чисел:", min_of_five(3, 8, -1, 5, 0))

def count_digits(number):
    return len(str(abs(number)))
print("Кількість цифр у числі 3456:", count_digits(3456))

def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]
print("Число 123321 є паліндромом?", is_palindrome(123321))
print("Число 421987 є паліндромом?", is_palindrome(421987))