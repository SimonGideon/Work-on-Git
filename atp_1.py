import os
import random
import string
n = int(input("Enter any Number: "))
n = n**n
path = os.getcwd()
count = 0
while True:

    for i in range(1, n):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        all = lower + digits
        length = 16
        name = "".join(random.sample(all, length))
        os.mkdir(path + f"\\{name}")
        count+=1
    break
print("Done!, You have Created", count, "Items")