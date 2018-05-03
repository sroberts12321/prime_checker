num_to_check = int(input("Please provide a number to check if prime: "))



def is_prime(possible_prime):
	placeholder = True

	if possible_prime == 2 or possible_prime == 1:
		placeholder = True

	for i in range(2, possible_prime):
		if (possible_prime % i) == 0:
			placeholder = False

	if placeholder == False:
		print("The number is not prime!")
		#print(i, "times", num_to_check//i, "is", num_to_check)
	else:
		print("That number is prime")


is_prime(num_to_check)