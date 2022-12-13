import os
import time
from sys import platform
from inputimeout import inputimeout

if platform == "linux" or platform == "linux2":
  clear = lambda: os.system('clear')
else:
  clear = lambda: os.system('cls')

def showMsg(message):
  print(message)

def inp (delay, text, enableAnswerDelay, n):
  all_words = []
  timeLeft = delay
  for _ in range(n):
    timeEnded = False
    if enableAnswerDelay:
      if timeLeft <= 0 and enableAnswerDelay:
        res = ''
        timeEnded = True
        break
      tStart = time.monotonic()
      try:
        res = inputimeout(prompt=text, timeout=timeLeft)
      except Exception:
        res = ''
        timeEnded = True
        break
      timeLeft =  timeLeft - (time.monotonic() - tStart) 
    
    else:
      res = input(text)
    all_words.append(res)
  reset = False
  return ' '.join(all_words), timeEnded, reset

def showStr(str, TimeDisplay):
  showMsg(str)
  time.sleep(TimeDisplay)
  clear()

