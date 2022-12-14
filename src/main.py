import os
import requests
import hashlib
import sys

folderName = 'data'

dataFileHash = "8c9d7f074a93b5d2e5ec73de66f04dfe17292796"
dataPath = "data/data.json"
dataUrl = "https://gist.githubusercontent.com/mkulik05/a56725ea4b1866db0453814b83434873/raw/0ef8fd8b2a5fe27519fc71958701639c2a332785/data.json"

settingsFileHash = "d25e9937905d3bba47347f91c3434e30cd8ce74d"
settingsPath = "data/settings.json"
settingsUrl = "https://gist.githubusercontent.com/mkulik05/a56725ea4b1866db0453814b83434873/raw/0ef8fd8b2a5fe27519fc71958701639c2a332785/settings.json"

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def downloadFile(url, path):
  try:
    response = requests.get(url)
    open(path, "wb").write(response.content)
  except:
    print("Check your internet connection and try again.")
    sys.exit()

if not os.path.exists(folderName):
  os.mkdir(folderName)

if not os.path.exists(dataPath):
  print("> Donwnloading required data")
  downloadFile(dataUrl, dataPath)

if not os.path.exists(settingsPath):
  print("> Donwnloading required settings")
  downloadFile(settingsUrl, settingsPath)

if hash_file(dataPath) != dataFileHash:
  print("> Donwnloading correct data")
  downloadFile(dataUrl, dataPath)

if hash_file(settingsPath) != settingsFileHash:
  print("> Donwnloading correct settings")
  downloadFile(settingsUrl, settingsPath)

from algo import launch
launch()