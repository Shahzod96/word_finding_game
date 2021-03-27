"""
Created on Fri Mar 26 2021

"S'OZ TOPISH O'YINI"

@author: acer
"""
from functions import play
print("\nАссалому алайкум! Келинг сўз топиш ўйинини ўйнаймиз.")
while True:
    play()
    result = int(input("\nЯна ўйнаймизми: ҳа(1)/йўқ(0)"))
    if result == 0:
        break

print("Ўйин тугади!")
