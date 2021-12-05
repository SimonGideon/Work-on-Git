# 80-100 - A
# 75-70 - A-
# 70-74 - B+
# 65-69 - B
# 55-59 - B-
# 50-54 - C+
# 45-49 - C
# 40-44 - C-
# 35-39 - D+
# 30-34 - D
# 25-29 - D-
# Rest E
class grading:
        def __init__(self, name, Maths, English, Chem, grade): 
            self.name = name
            self.Maths = Maths
            self.English = English
            self.Chem = Chem
            self.grade = grade

name = input("Enter name: ")
Maths = int(input("Enter Maths: "))
English = int(input("Enter English: "))
Chem = int(input("Enter Chem: "))
grade=[]
if Maths >=80:
	grade="A"
elif Maths>=75:
	grade="A-"
elif Maths>=70:
	grade="B+"
elif Maths>=65:
	grade="B"
elif Maths>=55:
	grade="B-"
elif Maths>=45:
	grade="C+"
elif Maths>=35:
	grade="C-"
elif Maths>=25:
	grade="C"
elif Maths>=15:
	grade="D"
elif Maths>=10:
	grade="D-"
else:
	grade="E"
sum = Maths + English + Chem
print(name, "----> Results")
print( "Mathematics: ",  grade)

