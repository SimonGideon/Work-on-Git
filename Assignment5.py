# School management System
# Registarar holds all the basic students details
class Registrar:
	def __init__(self, name, Reg_number, Id_number):
		self.name = name
		self.Reg_number = Reg_number
		self.Id_number = Id_number
"""Departmental covers only academic details of the 
student and inherits basic details from the registrar"""
class Departmentals(Registrar):
	def __init__(self, name, Reg_number, course, nameOfdepartment):
		Registrar.__init__(self, name, Reg_number)
		self.course = course
		self.nameOfdepartment = nameOfdepartment
"""Accounts departments is incahrge of the finance and inherits basix details
from the registrar and also can inheric academic details from the departmentals"""
class Accounts(Registrar):
	def __init__(self,name,Reg_number, course, fees_per_sem):
		super().__init__(name, Reg_number)
		self.course = course
		self.fees_per_sem = fees_per_sem
"""Health unit is the health sector which inherits details directly from the 
registrar"""
class HealthUnit(Registrar):
	def __init__(self, name, Reg_number, NHIF_no):
		Registrar.__init__(self, name, Reg_number)
		self.NHIF_no = NHIF_no
a = Registrar("Simon", "TU01", 89456)
print(a)
