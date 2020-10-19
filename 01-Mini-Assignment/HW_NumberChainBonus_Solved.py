# Initial variable conditional
user_play = "y"

# Set start number begin with 0
start_number = 0

# While loop
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = int(input("How many numbers? "))

    # Loop through the numbers. 
    for x in range(start_number, user_number + start_number):

        # Print each number in the range
        print(x)

    # Set the next start number as the last number of the loop
    start_number = start_number + user_number

    # Once complete...
    user_play = input("Continue the chain: (y)es or (n)o? ")

