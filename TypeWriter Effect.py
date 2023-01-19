import time
import sys

def write(s):
  for i in s:
    print(i, end="", flush=True)
    time.sleep(.09)

write("Hello! Your awake?\nI thought you were dead when I picked you up.\nNice to see a face with life in it. Were on our way to Therondria.\n... Hope your not a magic user.")