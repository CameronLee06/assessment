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

    ingredient_name = input("What is the name of the ingredient"
                            " you bought?... enter <xxx> to exit.")

    if ingredient_name == "xxx":
        break

    ingredient_amount = num_check("How much did you buy ?: ",
                                  "please enter a valid number")
    ingredient_price = num_check("How much did you pay?: ",
                                 "please enter a valid number")

    if 0 <= ingredient_price:
        pass
    elif ingredient_price == not_blank:
        print("Please enter a number...")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue
