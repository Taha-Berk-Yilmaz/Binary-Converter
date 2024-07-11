from tabulate import tabulate

operation_list = [['Operations', 'Definition'], ['1', 'Binary to Number'], ['2', 'Number to Binary'], ['3', 'String to Binary'], ['4', 'Binary to String'], ['99', 'Exit']]
table = operation_list
print("Hello! This program is a converter between Binary, numbers and strings.")
print(tabulate(table))


def toBinary(string):
	l,m=[],[]
	for i in string:
		l.append(ord(i))
	for i in l:
		m.append(int(bin(i)[2:]))
	return m

try:
	while True:
		user_input = input("Hello This is a binary converter program. Please enter the number of the operation: ")
		
		if user_input == '1':
			binary = input("Please enter your binary string here:")
			print(int(binary, 2))
		elif user_input == '2':
			number = int(input("Please enter your number string here:"))
			print(str(bin(number)[2::]))
		elif user_input == '4':
			a_binary_string = input("Please enter you binary string here:")
			binary_values = a_binary_string.split()
			ascii_string = ""

			for binary_value in binary_values:
				an_integer = int(binary_value, 2)
				ascii_character = chr(an_integer)
				ascii_string += ascii_character
			print(ascii_string)
		elif user_input == '3':
			string = input("Please enter your text here:")
			print(toBinary(string))
		elif user_input == "99":
			break
		else:
			print("Entered an invalid operation. Please enter again.\nIf you want to exit enter 99.")

except KeyboardInterrupt:
	print("\nExitted the program.")


"""
string = bin(38)
print(string[2::])
"""