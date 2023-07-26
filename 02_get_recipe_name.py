
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
# Get product name
product_name = not_blank("What is the name of the recipe? ", "Sorry - "
                  "the product name can't be blank, please try again")
how_many = num_check("How many people are you making for? ",
                     "Please enter an amount that is more than 0", int)