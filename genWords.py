import json
f = open("data/words.txt")
words = f.read().split('\n')
data = {}
for word in words:
  l = str(len(word))
  if int(l) in [5,6,7,8]:
    if l in data.keys():
      data[l].append(word)
    else:
      data[l] = []

f = open("data/data.json", "w")
f.write(json.dumps(data))
f.close()

