num_array = []

while True:
	user_input = int(input("please enter numbers :"))

	if user_input == 7:
		break

	num_array.append(user_input)

new_num_array = []

for i in num_array:
	if 25 <= i <= 99:
		new_num_array.append(i)
print("here is the numbers btween 25 and 99")
print(new_num_array)


