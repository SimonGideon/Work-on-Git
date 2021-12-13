# list
countries = ["Naigeria", "S.Africa", "Kenya", "China", "Germany", "Canada"]
for i in countries:
	print(i)
print(countries[1:4])
productions = ["Mango", "Banana", "Pineaple", "Carrots"]
# extend is used to add two lists into one.
countries.extend(productions)
print(countries)
# /append is used to add a value inside a list.
productions.append("Cherry")
# Insert is used to add a value in a list at a specific index.
productions.insert(1, "Orange")
# remove drops the specified b\value in the list.
productions.remove("Banana")
# clear drops all the values in a list.
# productions.clear()
productions.sort()
productions.reverse()
countries.pop(1)
print(countries)
print(productions)
print(len(productions))
# Index used to identify the index position of the specified value

print(countries.index("Kenya"))

names = ["Vicky", "Frank", ["Tonney", "Simon", "Jared", ["Jeff", "Joseph", "David", "Anne"]]]
print(names[2][0])
print(names[2][3][1])

for i in names:
	print(i)

names2=["Emmanuel", "Jared", ["Frank", "Irene", ["Peter", "Bruno"], "Paterson"]]
names.extend(names2[2][2])
names.insert(1, names2[2][3])
print(names)
print(names2[2][2].index("Peter"))


