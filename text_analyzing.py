original_text = input("Введите текст для анализа: ")
main_symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

clean_text = "" #  Пока пустая переменная-текст для сборки в неё отфильтрованных символов
for char in original_text:
    if char in main_symbols:
        clean_text += char.lower() #  Собираем текст только из цифр, пробелов и переведённых в нижний регистр букв

words = clean_text.split() #  Перевод фильтрованного текста в list-объект, т.е. список слов/чисел
#  print(words) #  строка для контроля

count = 0 #  1. Переменная-счётчик количества слов/чисел в тексте по списку слов
for element in words:
    count += 1
print("1. Количество слов/чисел:", count)

max_lenght = 0 #  Переменная для хранения текущей максимальной длины
biggest_word = "" # Переменная для хранения текущего максимального длинного слова
for element in words:
    if len(element) > max_lenght:
        max_lenght = len(element)
        biggest_word = element #  2. Первое самое длинное слово/число в тексте:
print("2. Первое самое длинное слово/число:", biggest_word)

vowels = "аеёиоуыэюя"
count_vowels = 0 #  Создаём переменную-счётчик гласных
for char in clean_text:
    if char in vowels:
        count_vowels +=1 #  3. Счётчик количества русских гласных в тексте
print("3. Количества русских гласных в тексте:", count_vowels)

repeated = {} # Создаеём dict объект
print("4. Количество повторов каждого слова:")
for element in words:
    if element in repeated:
        repeated[element] += 1 #  продолжаем считать, т.е. увеличиваем значение
    else:
        repeated[element] = 1 #  первый раз: создаётся элемент (ключ = слово, значение = 1)
for element in repeated:
    print(element, "--", repeated[element]) #  4. Выводит количество раз, которое каждое слово/число встречается в тексте.