number = int(input("Calculate the factorial of what number? : "))

def factorial(number):
	count = 1
	while number >= 1:
		count = count * number
		number -= 1
	return count

print(factorial(number))