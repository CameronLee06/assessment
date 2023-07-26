import pandas


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "n" or response == "no":
            return "no"

        else:
            print("Please answer yes / no")


def not_blank(prompt, error):
    while True:
        response = input(prompt)
        if response == "":
            print(f"{error}. Please try again.")
        else:
            return response


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
all_ingredient_name = []
all_ingredient_price = []
all_recipe_amount = []
all_bought_amount = []

recipe_dict = {
    "Ingredient": all_ingredient_name,
    "Recipe amount": all_recipe_amount,
    "Bought amount": all_bought_amount,
    "Ingredient price": all_ingredient_price
}

recipe_name = not_blank("What is the name of the recipe? ",
                        "Sorry - the product name can't be blank, please try again")
print()
how_many = num_check("How many people are you making for? ",
                     "Please enter an amount that is more than 0", int)
print()

while True:

    ingredient_name = not_blank("What is the name of the ingredient(s) that you are using?",
                                "Your answer can't be blank")

    if ingredient_name == 'xxx' and len(ingredient_name) > 0:
        break
    elif ingredient_name == 'xxx':
        print("You must enter an ingredient name")
        continue

    ingredient_price = num_check("How much did you buy the ingredient for?: $",
                                 "please enter a valid number", float)
    print()
    recipe_amount = not_blank("How much do you need? (in grams)?: ",
                              "please enter a valid number")
    print()
    bought_amount = not_blank("How much did you buy (in grams)?: ",
                              "please enter a valid number")
    print()
    ingredient_unit = input("Enter the unit of the ingredient: ")
    print()

while True:
    ingredient_name = input("Ingredient name: ")

    if ingredient_name == "xxx":
        break

    ingredient_name = input("Name: ")
    ingredient_price = float(input("Price: "))

# add content to lists!!
all_ingredient_name.append(ingredient_name)
all_recipe_amount.append(recipe_amount)
all_bought_amount.append(bought_amount)
all_ingredient_price.append(ingredient_price)

# make the panda..
recipe_panda_frame = pandas.DataFrame(recipe_dict)

recipe_panda_frame['Recipe Cost'] = \
    recipe_panda_frame['Price'] / 1.15

print(recipe_panda_frame)
