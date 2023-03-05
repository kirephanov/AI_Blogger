import numpy as np


def make_pairs(corpus):
    # Функция для генерации пар слов
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])


def generate_text(length):
    # Функция создает текст для записи
    text = open('text.txt', encoding='utf8').read()

    corpus = text.split()

    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    
    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = length

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    
    return chain