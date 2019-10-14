from Mod01 import TwitterCharacterLimit as Limit 
import math

text = "a" * 566

length = len(text)

if length % Limit == 0:
    print("There will be " + str(math.floor(length/Limit)) + " Tweet(s) total.")
else:
    print("There will be " + str((math.floor(length/Limit))+1) + " Tweet(s) total. The last Tweet will be shorter that 280.")