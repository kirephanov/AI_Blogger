from flask import Flask, render_template, redirect, url_for
import markovify
import numpy as np
import random

app = Flask(__name__)


# делаем новую функцию-генератор, которая определит пары слов
def make_pairs(corpus):
    # перебираем все слова в корпусе, кроме последнего
    for i in range(len(corpus)-1):
        # генерируем новую пару и возвращаем её как результат работы функции
        yield (corpus[i], corpus[i+1])


posts = []

@app.route("/")
def index():
    global posts

    page_posts = posts

    return render_template('index.html', page_posts=page_posts)


@app.route("/create-post")
def createPost():
    global posts
    post = ''

    # отправляем в переменную всё содержимое текстового файла
    text = open('text.txt', encoding='utf8').read()

    # разбиваем текст на отдельные слова (знаки препинания останутся рядом со своими словами)
    corpus = text.split()

    # вызываем генератор и получаем все пары слов
    pairs = make_pairs(corpus)

    # словарь, на старте пока пустой
    word_dict = {}

    # перебираем все слова попарно из нашего списка пар
    for word_1, word_2 in pairs:
        # если первое слово уже есть в словаре
        if word_1 in word_dict.keys():
            # то добавляем второе слово как возможное продолжение первого
            word_dict[word_1].append(word_2)
        # если же первого слова у нас в словаре не было
        else:
            # создаём новую запись в словаре и указываем второе слово как продолжение первого
            word_dict[word_1] = [word_2]
    
    # случайно выбираем первое слово для старта
    first_word = np.random.choice(corpus)

    # если в нашем первом слове нет больших букв 
    while first_word.islower():
        # то выбираем новое слово случайным образом
        # и так до тех пор, пока не найдём слово с большой буквой
        first_word = np.random.choice(corpus)

    # делаем наше первое слово первым звеном
    chain = [first_word]

    # сколько слов будет в готовом тексте
    n_words = random.randint(5, 25)

    # делаем цикл с нашим количеством слов
    for i in range(n_words):
        # на каждом шаге добавляем следующее слово из словаря, выбирая его случайным образом из доступных вариантов
        chain.append(np.random.choice(word_dict[chain[-1]]))

    # выводим результат
    post += ' '.join(chain)
    posts.insert(0, post)
    post = ''

    return redirect('/')