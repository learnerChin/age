driving = input("您是否會開車?")
if driving != "是" and driving != "否":
	print("只能輸入是或否")
	raise SystemExit
age = int(input("請問您的年紀"))
if driving == "是":
	if age >= 18:
		print("你通過測驗了")
	else:
		print("未成年偷開車")
elif driving == "否":
	if age >= 18:
		print("你可以考駕照了")
	else:
		age = 18 - age 
		print(f"再過{age}年就可以考了")