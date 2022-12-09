import time
import random
import os
import json
from sys import platform
from inputimeout import inputimeout

showDelay = 5               # время показа вопроса
enableAnswerDelay = True # ограничено ли время на ответ
answerDelay = 5             # время на ответ
needCorrectAnsws = 3        # количество правильным ответов для переходов далее
wordsInRound = 5            # количество слов в раундах 2-5


if platform == "linux" or platform == "linux2":
  clear = lambda: os.system('clear')
else:
  clear = lambda: os.system('cls')

f = open("data.json")
data = f.read()
words = json.loads(data)

def inp (text = '', delay = answerDelay):
  timeEnded = False
  if enableAnswerDelay:
    try:
      res = inputimeout(prompt=text, timeout=delay)
    except Exception:
      res = ''
      timeEnded = True
  else:
    res = input(text)
  return res, timeEnded

def showStr(str):
  print(str)
  time.sleep(showDelay)
  clear()

def invert(word):
  return word[::-1]

def strMatch(w1, w2):
  return w1.lower() == w2.lower()

def makeQuestion(arr):
  return ' '.join(arr)

def selectWord(len):
  return random.choice(words[str(len)])

def round1 ():
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      word = selectWord(i)
      showStr(word)
      userWord, timeEnded = inp('> ')
      if strMatch(word, invert(userWord)):
        print("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        if not timeEnded:
          print("Ответ неверный")
        else:
          print("Время вышло")
        correctAnsws = 0
      time.sleep(1)
      clear()

def round2(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      wordsSet = set(words)
      showStr(makeQuestion(words))
      userInp = inp('> ')
      userWords, timeEnded = set([w.lower() for w in userInp.split()])
      if userWords == wordsSet:
        print("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        if not timeEnded:
          print("Ответ неверный")
        else:
          print("Время вышло")
        correctAnsws = 0
      time.sleep(1)
      clear()


def round3(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      showStr(makeQuestion(words))
      userInp = inp('> ')
      userWords, timeEnded = [w.lower() for w in userInp.split()]
      if userWords == words:
        print("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        if not timeEnded:
          print("Ответ неверный")
        else:
          print("Время вышло")
        correctAnsws = 0
      time.sleep(1)
      clear()

def round4(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      wordsSet = set(words)
      showStr(makeQuestion(words))
      userInp = inp('> ')
      userWords, timeEnded = set([invert(w.lower()) for w in userInp.split()])
      if userWords == wordsSet:
        print("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        if not timeEnded:
          print("Ответ неверный")
        else:
          print("Время вышло")
        correctAnsws = 0
      time.sleep(1)
      clear()

def round5(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      showStr(makeQuestion(words))
      userInp, timeEnded = inp('> ')
      userWords = [invert(w.lower()) for w in userInp.split()]
      if userWords == words:
        print("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        if not timeEnded:
          print("Ответ неверный")
        else:
          print("Время вышло")
        correctAnsws = 0
      time.sleep(1)
      clear()

def main ():
  clear()
  round1()
  round2(wordsInRound)
  round3(wordsInRound)
  round4(wordsInRound)
  round5(wordsInRound)

main()
