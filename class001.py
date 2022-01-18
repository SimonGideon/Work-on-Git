count = 0
for i in range(10):
    num = eval(input("Enter the number: "))
    if num>10:
        count=count+1
    print("There are", count, 'numbers greater than 10')