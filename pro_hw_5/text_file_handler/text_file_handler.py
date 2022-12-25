import os
import string


# 1. Create a class that performs statistical processing of a text file - counting characters,
# words, sentences, etc. Determine the required attributes-data and attributes-methods
# in class for working with the text file.
class TextFileHandler:
    def __init__(self, file):
        self.__file = file

    def __setattr__(self, key, value):
        if not os.path.isfile(value):
            raise FileNotFoundError
        self.__dict__[key] = value

    def sum_symbols(self, number_lines_read=10_000, ignore_space=True):
        with open(self.__file, 'r') as f:
            summa = 0

            for key, line in enumerate(f):
                summa += len(line.strip())
                if ignore_space:
                    summa -= line.strip().count(' ')
                if self.stop_reading_text(key, number_lines_read):
                    break
            return summa

    def sum_words(self, number_lines_read=10_000, word_wrap=True):
        with open(self.__file, 'r') as f:
            summa = 0

            for key, line in enumerate(f):
                summa += len(tuple(i for i in line.strip().split() if i not in string.punctuation))
                if word_wrap and line[-2] == '-' and line[-3].isalpha():
                    summa -= 1
                if self.stop_reading_text(key, number_lines_read):
                    break
            return summa

    def sum_sentences(self, number_lines_read=10_000):
        with open(self.__file, 'r') as f:
            summa = 0

            for key, line in enumerate(f):
                summa += sum(line.count(punctuation_end_sentence) for punctuation_end_sentence in '.!?')
                if self.stop_reading_text(key, number_lines_read):
                    break
            return summa

    def quantity_characters(self, character, number_lines_read=10_000, ignore_register=False):
        with open(self.__file, 'r') as f:
            ignore_register = ignore_register and character.isalpha()
            summa = 0

            for key, line in enumerate(f):
                summa += line.lower().count(character.lower()) if ignore_register else line.count(character)
                if self.stop_reading_text(key, number_lines_read):
                    break
            return summa

    @staticmethod
    # instead of input - request to the user
    def stop_reading_text(number_of_lines, number_lines_read):
        return not (number_of_lines + 1) % number_lines_read and \
               input(f'Continue processing for next {number_lines_read} lines?[y/n]').lower() != 'y'
