from text_file_handler import TextFileHandler


if __name__ == '__main__':
    test_1 = TextFileHandler('text.txt')

    print(test_1.sum_symbols())
    print(test_1.sum_words())
    print(test_1.sum_words(word_wrap=False))
    print(test_1.sum_sentences())
    print(test_1.quantity_characters('П'))
    print(test_1.quantity_characters('П', 5_000, ignore_register=True))
