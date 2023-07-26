ingredient_prices = {}

def add_ingredient_price():
    ingredient = input("Enter the name of the ingredient: ")
    price = float(input("Enter the price of the ingredient: $"))
    ingredient_prices[ingredient] = price
    print(f"Ingredient '{ingredient}' with price ${price:.2f} has been added.")

def calculate_total_price():
    total_price = sum(ingredient_prices.values())
    print(f"The total price of all ingredients is ${total_price:.2f}.")

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

if __name__ == '__main__':
    main()