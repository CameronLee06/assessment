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

def not_blank(prompt, error):
    while True:
        response = input(prompt)
        if response == "":
            print(f"{error}. Please try again.")
        else:
            return response

while True:

    ingredient_unit = input("What unit would you like to use?"
                            " (KG, G, ML...)... enter <xxx> to exit.")
    
    if ingredient_unit == "xxx":
        break


    if 0 <= ingredient_unit:
        pass
    elif ingredient_unit == not_blank:
        print("Please enter a valid unit...")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue