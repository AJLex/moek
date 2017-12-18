# функция считает количество слов в предложении, разделённых пробелом
def count_word(sentence):
    if isinstance(sentence, str) is True: #  Проверка типа входных данных
        return len(sentence.split())
    else:
        return 'Не верные данные'


if __name__ == '__main__':
    sentence = 'Hello, world!'
    print(count_word(sentence))
    sentence = 'I love python'
    print(count_word(sentence))
    sentence = 1
    print(count_word(sentence))
