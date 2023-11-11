# Author: Justin Gabotero -- STM113

def evenString(e: str):
  z = []
  for i in range(len(list(e))):
    if i%2 == 0:
      z.append(list(e)[i])
  return z

print(evenString("pynative"))