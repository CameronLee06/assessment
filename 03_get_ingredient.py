# checks that users input is not blank
def not_blank(prompt, error):
    while True:
        response = input(prompt)
        if response == "":
            print(f"{error}. Please try again.")
        else:
            return response


# checks that input is either a float or an
# integer that is more than zero. Takes in custom error messages
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
while True:
    print("Press <xxx> when you have all your ingredients")
    print()

    # ask user if they want to end the program
    again = input("What ingredient would you like to use?")

    # if the user presses <xxx> end the loop
    if again == "xxx":
        break

    print()
