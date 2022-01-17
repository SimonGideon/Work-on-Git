list = [78, "b", 56, 1, "f", 5, 7, 8, 63, "a"]
for i in range(len(list)// 2):
	list[i], list[-1 - i] = list[-1 - i], list[i]
print(list)