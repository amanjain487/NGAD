import os
import random
import string
import sys

os.makedirs("TXT Files", exist_ok=True)
try:
    n = int(sys.argv[1])
except IndexError:
    n = 25

os.chdir("TXT Files")
files = os.listdir()
for file in files:
    os.remove(file)

for i in range(n):
    f = open("Random File " + str(i) + ".txt", "w")
    byte_size = random.randint(40000, 500000)
    for _ in range(byte_size):
        f.write(random.choice(string.ascii_letters + string.digits))
    f.close()

os.chdir("..")
