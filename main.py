def hello():
	print ("Hello World!")


def sum(a, b):
	return a + b

def multiply(a, b):
	return a * b

def main():
	hello()
	print ("Sum of 5 and 3 = {}".format(sum(5, 3)) )
	print ("Product of 5 and 3 = {}".format(multiply(5, 3)))
	print ("Product of 5 and 5 = {}".format(multiply(5, 5)))


if __name__ == '__main__':
	main()