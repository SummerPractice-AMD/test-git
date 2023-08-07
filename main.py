def hello():
	print ("Hello World!")


def sum(a, b):
	return a + b



def main():
	hello()
	print ("Sum of 5 and 3 = {}".format(sum(5, 3)) )


if __name__ == '__main__':
	main()