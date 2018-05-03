string = input("Please input a word: ")
new_array = []
reverse_array = []

for i in string:
	new_array.append(i)

for i in new_array[::-1]:
	reverse_array.append(i)

if new_array == reverse_array:
	print("Your input was a palindrome!")
else:
	print("Your input was not a palindrome!")