import random
import string
import sys
import os

f = open("Random File.txt", "w")
no_of_lines = random.randint(15, 300)
for _ in range(no_of_lines):
    no_of_chars = random.randint(10, 20)
    for _ in range(no_of_chars):
        f.write(random.choice(string.ascii_letters + string.digits))
    f.write("\n")
f.close()
