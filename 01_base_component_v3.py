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


def string_checker(question, num_letters, valid_responses, ):
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def format_currency(x):
    return "${:,.2f}".format(x)


# main routine goes here
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

recipe_name = not_blank("What is the name of the recipe? ",
                        "Sorry - the product name can't be blank, please try again")
print()
how_many = num_check("How many people are you making for? ",
                     "Please enter an amount that is more than 0", int)
print()

recipe_amount = ""
bought_amount = ""
ingredient_price = ""
cost_to_make = ""

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

    print(f"You have entered that {ingredient_name} costs: {ingredient_price}")
    print()

    recipe_amount = num_check("How much do you need? (in grams)?: ",
                              "please enter a valid number", float)
    print(f"You have entered that you need {recipe_amount}g for your recipe")
    print()

    bought_amount = num_check("How much did you buy (in grams)?: ",
                              "please enter a valid number", float)

    print(f"You have entered that you bought {bought_amount} of {ingredient_name}")
    print()

    ingredient_unit = input("Enter the unit of the ingredient: ")
    print(f"The unit is in grams. ")

    cost_per_unit = (ingredient_price / bought_amount * recipe_amount)

    # add content to lists!!
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
