time = int(input("Number of Seconds: "))
minutes = time//60
seconds =  time%60
if minutes>=60:
	n = minutes//60 
	m = minutes%60
	if n>=24:
		r = n//24
		s = n%24
		print(r, "Days", s, "hours", m, "Minutes", seconds, "Seconds")
	else:
		print(n, "hours", m, "Minutes", seconds, "Seconds")
else:
	print(minutes, "Minutes", seconds, "Seconds")