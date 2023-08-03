import pandas


# Asks the user yes / no
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


# checks that user response is not blank
def not_blank(prompt, error):
    while True:
        response = input(prompt)
        if response == "":
            print(f"{error}. Please try again.")
        else:
            return response


# checks user enters an integer to a given question
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


# Finds if the user has entered a specific word / letter
def string_checker(question, num_letters, valid_responses, ):
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# currency formatting function
def format_currency(x):
    return "${:,.2f}".format(x)


# main routine goes here

# Set up dictionaries and lists
all_ingredient_name = []
all_ingredient_price = []
all_recipe_amount = []
all_bought_amount = []
all_cost_to_make = []

recipe_dict = {
    "Ingredient": all_ingredient_name,
    "Recipe amount": all_recipe_amount,
    "Bought amount": all_bought_amount,
    'Price': all_ingredient_price,
    "Cost to make": all_cost_to_make,
}
# Asks the user for the name of recipe
recipe_name = not_blank("What is the name of the recipe? ",
                        "Sorry - the product name can't be blank, please try again")
print()

# Asks the user for the amount of servings
how_many = num_check("How many people are you making for? ",
                     "Please enter an amount that is more than 0", int)
print()

recipe_amount = ""
bought_amount = ""
ingredient_price = ""
cost_to_make = ""

# loop to get ingredient name, bought and needed amount, price and unit
while True:

    ingredient_name = not_blank("What is the name of the ingredient(s) that you are using?",
                                "Your answer can't be blank")

    if ingredient_name == 'xxx' and len(all_ingredient_name) > 0:
        break
    elif ingredient_name == 'xxx':
        print("You must enter an ingredient name")
        continue

    print(f"You have entered {ingredient_name} as an ingredient")
    print()

    ingredient_price = num_check("How much did you buy the ingredient for?: $",
                                 "please enter a valid number", float)

    print(f"You have entered that {ingredient_name} costs: ${ingredient_price}")
    print()

    ingredient_unit = input("Enter the unit of the ingredient (has "
                            "to be either g, ml or blank): ")
    print(f"The unit is in {ingredient_unit}")

    recipe_amount = num_check(f"How much {ingredient_name} do you need?",
                              "please enter a valid number", float)

    print(f"You have entered that you need {recipe_amount}{ingredient_unit}"
          f" for your recipe")
    print()

    bought_amount = num_check("How much did you buy?: ",
                              "please enter a valid number", float)

    print(f"You have entered that you bought {bought_amount}{ingredient_unit}"
          f" of {ingredient_name}")
    print()

    cost_per_unit = (ingredient_price / bought_amount * recipe_amount)

    # add content to lists
    all_ingredient_name.append(ingredient_name)
    all_recipe_amount.append(recipe_amount)
    all_bought_amount.append(bought_amount)
    all_ingredient_price.append(ingredient_price)
    all_cost_to_make.append(cost_per_unit)

# make the panda..
recipe_panda_frame = pandas.DataFrame(recipe_dict)

# calculate the cost of each item and the total cost
total_cost = recipe_panda_frame["Cost to make"].sum()
cost_per_serving = total_cost / how_many
print(recipe_panda_frame)
print("Total Cost = ${:.2f}".format(total_cost))
print("Cost Per Serving = ${:.2f}".format(cost_per_serving))
