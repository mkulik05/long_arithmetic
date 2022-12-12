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

def inp (delay, text, enableAnswerDelay):
  timeEnded = False
  if enableAnswerDelay:
    try:
      res = inputimeout(prompt=text, timeout=delay)
    except Exception:
      res = ''
      timeEnded = True
  else:
    res = input(text)
  reset = False
  return res, timeEnded, reset

def showStr(str, TimeDisplay):
  showMsg(str)
  time.sleep(TimeDisplay)
  clear()

