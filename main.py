# -*- coding: utf-8 -*-
import sys
import string


class Data:
    def __init__(self, most_frequent_word, word_count, char_count):
        self.most_frequent_word = most_frequent_word
        self.word_count = word_count
        self.char_count = char_count

    def print(self):
        print("Самое популярное слово: ", self.most_frequent_word)
        print("Количество слов: ", self.word_count)
        print("Количество символов: ", self.char_count)


def read(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Файл не найден")
        return ""
    except PermissionError:
        print("Файл не открывается")
        return ""
    except ValueError:
        print("Файл пустой")
        return ""


def task(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    word_freq = {}
    for word in words:
        word = word.lower().strip(string.punctuation)
        if word:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        else:
            word_count -= 1
    if word_count > 0:
        most_frequent_word = max(word_freq, key=word_freq.get)
        res = Data(most_frequent_word, word_count, char_count)
    else:
        res = Data("", 0, char_count)
    return res


file_name = input("Название файла: ")
data = task(read(file_name))
data.print()
