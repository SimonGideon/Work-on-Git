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
sum = Maths + English + Chem
Mean = sum//3
grade=[]
if  Mean >=80:
	grade="A"
elif  Mean>=75:
	grade="A-"
elif  Mean>=70:
	grade="B+"
elif  Mean>=65:
	grade="B"
elif  Mean>=55:
	grade="B-"
elif  Mean>=45:
	grade="C+"
elif  Mean>=35:
	grade="C-"
elif  Mean>=25:
	grade="C"
elif  Mean>=15:
	grade="D"
elif  Mean>=10:
	grade="D-"
else:
	grade="E"
print(name, "----> Results")
print( "Mean Grade: ",  grade)

