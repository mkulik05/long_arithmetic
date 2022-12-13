import os
import requests

folderName = 'data'
dataPath = "data/data.json"
dataUrl = "https://gist.githubusercontent.com/mkulik05/a56725ea4b1866db0453814b83434873/raw/0ef8fd8b2a5fe27519fc71958701639c2a332785/data.json"
settingsPath = "data/settings.json"
settingsUrl = "https://gist.githubusercontent.com/mkulik05/a56725ea4b1866db0453814b83434873/raw/0ef8fd8b2a5fe27519fc71958701639c2a332785/settings.json"

if not os.path.exists(folderName):
  os.mkdir(folderName)

if not os.path.exists(dataPath):
  print("> Donwnloading required data")
  response = requests.get(dataUrl)
  open(dataPath, "wb").write(response.content)

if not os.path.exists(settingsPath):
  print("> Donwnloading required settings")
  response = requests.get(settingsUrl)
  open(settingsPath, "wb").write(response.content)
 
from algo import launch
launch()