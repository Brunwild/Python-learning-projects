a = input("Введите слово: ").lower()
msg = "палиндром" if a == a[::-1] else "не палиндром"
print(msg)