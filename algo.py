import time
import random
import os
import json

from gui import clear, inp, showMsg, showStr 

needCorrectAnsws = 3        # количество правильным ответов для переходов далее
wordsInRound = 5            # количество слов в раундах 2-5
TimeBetweenStages = 3


f = open("data/data.json")
data = f.read()
words = json.loads(data)

f = open("data/settings.json")
data = f.read()
settings = json.loads(data)

def invert(word):
  return word[::-1]

def strMatch(w1, w2):
  return w1.lower() == w2.lower()

def makeQuestion(arr):
  return ' '.join(arr)

def selectWord(len):
  return random.choice(words[str(len)])



def stage1 ():
  global ResetNum, ResetsN, enableAnswerDelay
  madeErrs = 0
  for i in range(5, 6):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws and madeErrs < ErrNum + 0.1:
      word = selectWord(i)
      showStr(word, TimeDisplay)
      userWord, timeEnded, reset = inp(TimeInput, '> ', enableAnswerDelay, 1)
      if reset and ResetAvailable and ResetsN < ResetNum:
        ResetsN += 1
      else:
        if strMatch(word, invert(userWord)):
          showMsg("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
          correctAnsws += 1
        else:
          if not timeEnded:
            showMsg("Ответ неверный")
          else:
            showMsg("Время вышло")
          madeErrs += 1
          correctAnsws = 0
          time.sleep(ErrPause)
      time.sleep(TimePrepWord)
      clear()
    if madeErrs >= ErrNum - 0.1:
      return False
    if ClearErrsEachInRound:
      madeErrs = 0
    time.sleep(TimeBetweenRounds)
  return True

def stage2(wordsN = wordsInRound):
  global ResetNum, ResetsN, enableAnswerDelay
  madeErrs = 0
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws and madeErrs < ErrNum + 0.1:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      wordsSet = set(words)
      showStr(makeQuestion(words), TimeDisplay)
      userInp, timeEnded, reset = inp(TimeInput, '> ', enableAnswerDelay, 5)
      userWords = set([w.lower() for w in userInp.split()])
      if reset and ResetAvailable and ResetsN < ResetNum:
        ResetsN += 1
      else:
        if userWords == wordsSet:
          showMsg("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
          correctAnsws += 1
        else:
          if not timeEnded:
            showMsg("Ответ неверный")
          else:
            showMsg("Время вышло")
          madeErrs += 1
          correctAnsws = 0
          time.sleep(ErrPause)
      time.sleep(TimePrepWord)
      clear()
    if madeErrs >= ErrNum - 0.1:
      return False
    if ClearErrsEachInRound:
      madeErrs = 0
    time.sleep(TimeBetweenRounds)
  return True


def stage3(wordsN = wordsInRound):
  global ResetNum, ResetsN, enableAnswerDelay
  madeErrs = 0
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws and madeErrs < ErrNum + 0.1:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      showStr(makeQuestion(words), TimeDisplay)
      userInp, timeEnded, reset = inp(TimeInput, '> ', enableAnswerDelay, 5)
      userWords = [w.lower() for w in userInp.split()]
      if reset and ResetAvailable and ResetsN < ResetNum:
        ResetsN += 1
      else:
        if userWords == words:
          showMsg("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
          correctAnsws += 1
        else:
          if not timeEnded:
            showMsg("Ответ неверный")
          else:
            showMsg("Время вышло")
          madeErrs += 1
          correctAnsws = 0
          time.sleep(ErrPause)
      time.sleep(TimePrepWord)
      clear()
    if madeErrs >= ErrNum - 0.1:
      return False
    if ClearErrsEachInRound:
      madeErrs = 0
    time.sleep(TimeBetweenRounds)
  return True

def stage4(wordsN = wordsInRound):
  global ResetNum, ResetsN, enableAnswerDelay
  madeErrs = 0
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws and madeErrs < ErrNum + 0.1:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      wordsSet = set(words)
      showStr(makeQuestion(words), TimeDisplay)
      userInp, timeEnded, reset = inp(TimeInput, '> ', enableAnswerDelay, 5)
      userWords = set([invert(w.lower()) for w in userInp.split()])
      if reset and ResetAvailable and ResetsN < ResetNum:
        ResetsN += 1
      else:
        if userWords == wordsSet:
          showMsg("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
          correctAnsws += 1
        else:
          if not timeEnded:
            showMsg("Ответ неверный")
          else:
            showMsg("Время вышло")
          madeErrs += 1
          correctAnsws = 0
          time.sleep(ErrPause)
      time.sleep(TimePrepWord)
      clear()
    if madeErrs >= ErrNum - 0.1:
      return False
    if ClearErrsEachInRound:
      madeErrs = 0
    time.sleep(TimeBetweenRounds)
  return True

def stage5(wordsN = wordsInRound):
  global ResetNum, ResetsN, enableAnswerDelay
  madeErrs = 0
  for i in range(5, 9):
    correctAnsws = 0
    while correctAnsws < needCorrectAnsws and madeErrs < ErrNum + 0.1:
      words = []
      for _ in range(wordsN):
        words.append(selectWord(i))
      showStr(makeQuestion(words), TimeDisplay)
      userInp, timeEnded, reset = inp(TimeInput, '> ', enableAnswerDelay, 5)
      userWords = [invert(w.lower()) for w in userInp.split()]
      if reset and ResetAvailable and ResetsN < ResetNum:
        ResetsN += 1
      else:
        if userWords == words:
          showMsg("Отвечено {}/{}".format(correctAnsws + 1, needCorrectAnsws))
          correctAnsws += 1
        else:
          if not timeEnded:
            showMsg("Ответ неверный")
          else:
            showMsg("Время вышло")
          madeErrs += 1
          correctAnsws = 0
          time.sleep(ErrPause)
      time.sleep(TimePrepWord)
      clear()
    if madeErrs >= ErrNum - 0.1:
      return False
    if ClearErrsEachInRound:
      madeErrs = 0
    time.sleep(TimeBetweenRounds)
  return True

def selectDifficulty():
  d = ""
  while d not in ["1", "2", "3"]:
    d = input("Select difficulty from 1 to 3: ")
  return d
  

rounds = [stage1, stage2, stage3, stage4, stage5]
def main ():
  global TimeDisplay, TimeInput, ErrNum, ErrsInRoundOrStage, ErrPause, ResetsN, enableAnswerDelay
  global ResetAvailable, ResetNum, TimePrepWord, TimeBetweenRounds, ClearErrsEachInRound
  difficulty = selectDifficulty()
  clear()
  for i in range(len(rounds)):
    currConfig = settings["stage" + str(i + 1)]["difficulty" + str(difficulty)]
    
    TimeDisplay = currConfig["TimeDisplay"]
    TimeInput = currConfig["TimeInput"]
    ErrNum = float(currConfig["ErrNum"])
    ClearErrsEachInRound = currConfig["ClearErrsEachInRound"]
    ErrPause = currConfig["ErrPause"]
    ResetAvailable = currConfig["ResetAvailable"]
    ResetNum = currConfig["ResetNum"]
    TimePrepWord = currConfig["TimePrepWord"]
    TimeBetweenRounds = currConfig["TimeBetweenRounds"]
    enableAnswerDelay = currConfig["enableAnswerDelay"]
    ResetsN = 0
    completed = rounds[i]()
    if not completed:
      return False
  
    if i != len(rounds) - 1:
      time.sleep(TimeBetweenStages)

  return True

def launch():
  clear()
  won = main()
  if won:
    showMsg("Вы победили!!!")
  else:
    showMsg("Вы проиграли")
