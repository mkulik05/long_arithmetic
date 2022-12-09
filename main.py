import time
import random
import os

delay = 5 # in seconds
needCorrectAnsws = 3

# clear = lambda: os.system('cls')
clear = lambda: os.system('clear')

def showStr(str):
  print(str)
  clear()

def invert(word):
  return word[::-1]

def strMatch(w1, w2):
  return w1.toLoweCase() == w2.toLoweCase()

words = {5: ["abcde"], 6: ["abcdef"], 7: ["abcdefg"], 8: ["abcdefgh"]}

def makeQuestion(arr):
  return ' '.join(arr)

def selectWord(len):
  return random.choice(words[len])

def round1 ():
  for i in range(5, 9):
    word = selectWord(i)
    showStr(word)
    userWord = input()
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      if strMatch(word, userWord):
        print("Correct, {}/{}".format(correctAnsws, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0
      
def round2(wordsN):
  for i in range(5, 9):
    words = []
    for _ in range(wordsN):
      words.append(selectWord(i))
    wordsSet = set(words)
    showStr(makeQuestion(words))
    userInp = input()
    userWords = set([w.toLowerCase() for w in userInp.split()])
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws:
      if userWords == wordsSet:
        print("Correct, {}/{}".format(correctAnsws, needCorrectAnsws))
        correctAnsws += 1
      else:
        print("Incorrect")
        correctAnsws = 0


def main ():
  round1()
  round2(5)
  print(invert('12as'))

main()
