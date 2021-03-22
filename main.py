import os

def get_words(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def words_into_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

def count_words(filename):
    if not os.path.exists(filename):
        print("Неудалось открыть файл")
    else:
        words = get_words(filename)
        words_dict = words_into_dict(words)
        print("Количество слов: ", len(words))
        print("Количество уникальных слов: ", len(words_dict))
        print("Все использованные слова:")
        for word in words_dict:
            print(word, words_dict[word])
