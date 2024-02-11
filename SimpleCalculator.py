import math

def calc(x, y, ops):
	try:
		x = float(x)
		y = float(y)
	except ValueError:
		return "Invalid input. Please enter numeric values."

     

	if ops not in "+-*/^r%mp":
		return "Only in + - / * please !!!  "

	if ops == "+":
		return f"{x} {ops} {y} = {x + y}"
	elif ops == "-":
		return f"{x} {ops} {y} = {x - y}"
	elif ops == "/":
		if y == 0:
			return "Cannot divide by zero. Please choose a non-zero divisor."
		return f"{x} {ops} {y} = {x / y}"
	elif ops == "*":
		return f"{x} {ops} {y} = {x * y}"
	elif ops == "^":
		return f"{x} {ops} {y} = {x ** y}"
	elif ops == "r":
		return f"Square root of {x} = {math.sqrt(x)}"
	elif ops == "m":
		return f"{x} {ops} {y} = {x % y}"
	elif ops == "p":
		return f"{x} percent of {y} = {x / 100 * y}"

while True:

	x = input("Please enter first number: ")
	y = input("Please enter second number: ")
	ops = input("Choose between + - / * ^ (for exponentiation) r (for square root) m (for modulo) or p (for percentage): ")


	print(calc(x,y,ops))






