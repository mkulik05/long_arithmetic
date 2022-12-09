import time
import random
import os

delay = 5 # in seconds
needCorrectAnsws = 3
wordsInRound = 5

words = {5: ["abcde"], 6: ["abcdef"], 7: ["abcdefg"], 8: ["abcdefgh"]}

# clear = lambda: os.system('cls')
clear = lambda: os.system('clear')

def showStr(str):
  print(str)
  time.sleep(delay)
  clear()

def invert(word):
  return word[::-1]

def strMatch(w1, w2):
  return w1.lower() == w2.lower()

def makeQuestion(arr):
  return ' '.join(arr)

def selectWord(len):
  return random.choice(words[len])

def round1 ():
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      word = selectWord(i)
      showStr(word)
      userWord = input()
      if strMatch(word, invert(userWord)):
        print("Correct, {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0
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
      userInp = input()
      userWords = set([w.lower() for w in userInp.split()])
      if userWords == wordsSet:
        print("Correct, {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0
      clear()


def round3(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      showStr(makeQuestion(words))
      userInp = input()
      userWords = [w.lower() for w in userInp.split()]
      if userWords == wordsSet:
        print("Correct, {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0
      clear()

def round4(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      showStr(makeQuestion(words))
      userInp = input()
      userWords = [invert(w.lower()) for w in userInp.split()]
      if userWords == wordsSet:
        print("Correct, {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0
      clear()

def round5(wordsN):
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      wordsSet = set(words)
      showStr(makeQuestion(words))
      userInp = input()
      userWords = set([invert(w.lower()) for w in userInp.split()])
      if userWords == wordsSet:
        print("Correct, {}/{}".format(correctAnsws + 1, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0
      clear()

def main ():
  round1()
  round2(wordsInRound)
  round3(wordsInRound)
  round4(wordsInRound)
  round5(wordsInRound)

main()
