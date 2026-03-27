def input_text_filter(): #  Ввод текста и предварительная фильтрация
    original_text = input("Введите текст для анализа: ")
    #  "Лишние" символы, которые не будем считать при анализе
    not_text = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    #  Собираем текст без "лишних" символов; переводим в нижний регистр
    clean_text = ''.join(ch for ch in original_text if ch not in not_text or ch == ' ').lower()
    return clean_text


def word_count(clean_text): #  Считаем количество слов, ориентируясь на прбелы-разделители
    words = clean_text.split() #  Список слов
    count = len(words)
    print("1. Количество слов/чисел:", count)
    return words


def longest_word_finding(words):
    biggest_word = "" #  Переменная для хранения текущего максимального длинного слова
    for element in words:
        if len(element) > len(biggest_word):
            biggest_word = element
    print("2. Первое самое длинное слово/число:", biggest_word)


def russian_vowel_counter(clean_text): #  Счётчик количества русских гласных в тексте
    vowels = "аеёиоуыэюя"
    count_vowels = 0 #  Создаём переменную-счётчик гласных
    for char in clean_text:
        if char in vowels:
            count_vowels +=1
    print("3. Количества русских гласных в тексте:", count_vowels)


def word_duplication_counting(words):
    repeated = {} # Создаеём dict объект
    print("4. Количество повторов каждого слова/числа:")
    for element in words:
        if element in repeated:
            repeated[element] += 1 #  продолжаем считать, т.е. увеличиваем значение
        else:
            repeated[element] = 1 #  первый раз: создаётся элемент (ключ = слово, значение = 1)
    for element in repeated:
        print("\t", element, "--", repeated[element])


clean_text = input_text_filter()
words = word_count(clean_text)
longest_word_finding(words)
russian_vowel_counter(clean_text)
word_duplication_counting(words)