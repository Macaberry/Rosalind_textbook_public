import os

prefix = "BA3"
n = 0
ASCII_big = [chr(i) for i in range(65, 65+n)]

for j in range(n):
    filename = prefix + ASCII_big[j] + ".py"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("")
