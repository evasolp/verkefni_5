
#Step 1: n is a number that we get from the user as a input.
#Step 2: We want to find the first n nubers of our sequence.
#Step 3: If we look at the first 7 given numbers of the sequence we can see that it starts with 1, 2 and 3 and each number after that is the sum of the last 3 numbers
#Step 4: We know that the first 3 numbers are 1, 2 and 3 so if the user inputs 1, 2 or 3 we know the numbers to print out.
#Step 5: If the user inputs 4 or higher we have to find the sum of the last 3 numbers.

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num1 = 1
num2 = 2
num3 = 3
counter = 1

while counter <= n:
    if counter > 3:
        number_in_seq = num1 + num2 + num3
        print(number_in_seq)
        num1 = num2
        num2 = num3
        num3 = number_in_seq
    else:
        number_in_seq = counter
        print(number_in_seq)
    counter += 1

    