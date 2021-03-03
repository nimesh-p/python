def check_armstrong():
	num = int(input("Enter the number to check armstrong or not: "))
	if (num < 0):
		return "Enter valid number"
	power = len(str(num))
	sum = 0
	temp = num
	while temp > 0:
		nums = temp % 10
		sum += nums ** power
		temp //= 10
	if num == sum:
		return "Is armstrong number"
	else:
		return "Is not an armstrong number"
