# this is just to check it
# one line is added
while True:
	try:
		x=int(input("Please enter a number: "))
		break
	except ValueError:
		print("OOps! That was no valid number. Try again...")

