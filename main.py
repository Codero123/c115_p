import os
import time

source = "C:/Users/Tk/Desktop/20GAMES.txt"

dest = "C:/Users/Tk/Desktop/20_GAMES.txt"

print("Renaming source path to dest path...")
time.sleep(1)
os.rename(source, dest)
print("Successfully renamed source path to dest path!")