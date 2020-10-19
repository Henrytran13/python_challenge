# Initial variable conditional
user_play = "y"

# While loop
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = int(input("How many numbers? "))

    # Loop through the numbers
    for x in range(user_number):

        # Print each number in the range
        print(x)

    # Once complete, ask player continue pay or not
    user_play = input("Continue: (y)es or (n)o? ")
