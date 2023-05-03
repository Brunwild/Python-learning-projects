# объявление функции
def is_palindrome(text):
    symbol = [',', '.', '!', '?', '-', ' ']
    for x in symbol:
        text = text.replace(x, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))