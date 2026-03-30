def input_text_filter(original_text): # Предварительная фильтрация
    #  Введённый original_text может содержать только буквы, цифры, пробелы и символы,
    #  указанные в переменной punctuation_mark.
    #  "Лишние" символы, которые не будем считать при анализе:
    punctuation_mark = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    #  Собираем текст без "лишних" символов; переводим в нижний регистр
    clean_text = ''.join(char for char in original_text if char not in punctuation_mark or char == ' ').lower()
    return clean_text


def word_count(clean_text): #  Считаем количество слов, ориентируясь на пробелы-разделители
    words = clean_text.split() #  Список слов
    count = len(words) # Количество слов
    return count, words


def longest_word_finding(words):
    longest_word = "" #  Переменная для хранения текущего максимального длинного слова
    for element in words:
        if len(element) > len(longest_word):
            longest_word = element
    return longest_word


def russian_vowel_counter(clean_text): #  Счётчик количества русских гласных в тексте
    vowels = "аеёиоуыэюя"
    count_vowels = 0 #  Создаём переменную-счётчик гласных
    for char in clean_text:
        if char in vowels:
            count_vowels +=1
    return count_vowels


def word_duplication_counting(words): #  Выводит количество раз, которое каждое слово встречается в тексте
    repeated = {} # Создаём dict объект
    for element in words:
        if element in repeated:
            repeated[element] += 1 #  продолжаем считать, т.е. увеличиваем значение
        else:
            repeated[element] = 1 #  первый раз: создаётся элемент (ключ = слово, значение = 1)
    for element in repeated: #  Выводим dict объект: каждую пару ключ-значение -- с новой строки
        print("\t", element, "--", repeated[element])


original_text = input("Введите текст для анализа: ")
clean_text = input_text_filter(original_text)
count, words = word_count(clean_text)
longest_word = longest_word_finding(words)
count_vowels = russian_vowel_counter(clean_text)
print("1. Количество слов/чисел: ", count)
print("2. Первое самое длинное слово/число:", longest_word)
print("3. Количества русских гласных в тексте:", count_vowels)
print("4. Количество повторов каждого слова/числа:")
word_duplication_counting(words)