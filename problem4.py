#WAP to take marks from user to check user able to take admission in college or not. If marks is less than 60 then don't allow to take admission
marks = int(input("Enter your marks - "))
if (marks < 60):
	print("Sorry! you cannot take admission. you need "+ str(60-marks)+ " numbers more to get admission")
else:
	print("You can take admission")