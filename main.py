import os
try:
  import inputimeout
except:
  os.system('pip install inputimeout')

from algo import launch
launch()