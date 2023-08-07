def hello():
	print ("Hello World!")


def sum(a, b, c):
	return a + b + c

def multiply(a, b):
	return a * b

def subtract(a, b):
	return a - b


def main():
	hello()
	print ("Sum of 5 and 3 = {} and a - b = {}".format(sum(5, 3, 3), subtract(a, b)) )
	print ("Product of 5 and 3 = {}".format(multiply(5, 3)))
	print ("Product of 5 and 5 = {}".format(multiply(5, 5)))


if __name__ == '__main__':
	main()