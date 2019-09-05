#Step 1: We take a postive integer in from the user
#Step 2: The first input is our maximum int at the moment because it is the only one
#Step 3: Then we take another positive integer in from the user
#Step 4: If the new integer is higher than the maximum int then the new integer becomes the maximum int, otherwise the maximum int will stay the same
#Step 5: Repeat step 3 and 4 until we get a negative input from the user
#Step 6: When we get a negative input from the user, we print out the maximum int

num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input('Input a number: '))

print("The maximum is", max_int)    # Do not change this line