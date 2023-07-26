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
        response = num_type(input(question))

        if response <= 0:
            print(error)
        else:
            return response


def main():
    while True:
        print("\nIngredient Price Management")
        print("1. Add an ingredient price")
        print("2. Calculate total price")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_ingredient_price()
        elif choice == "2":
            calculate_total_price()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def calculate_total_price():
    total_price = sum(info["price"] for info in ingredient_prices.values())
    print(f"The total price of all ingredients is ${total_price:.2f}.")


def add_ingredient_price():
    ingredient_name = input("Enter the name of the ingredient: ")
    ingredient_price = float(input("Enter the price of the ingredient: $"))
    ingredient_unit = input("Enter the unit of the ingredient: ")
    ingredient_prices[ingredient_name] = {"price": ingredient_price, "unit": ingredient_unit}
    print(f"Ingredient '{ingredient_name}' with price ${ingredient_price:.2f} per {ingredient_unit} has been added.")


# main routine goes here
product_name = not_blank("What is the name of the recipe? ",
                         "Sorry - the product name can't be blank, please try again")
print()
how_many = num_check("How many people are you making for? ", "Please enter an amount that is more than 0", int)
print()

ingredient_prices = {}

if __name__ == '__main__':
    main()
