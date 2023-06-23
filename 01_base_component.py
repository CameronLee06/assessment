
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


show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they want to see how to make a burger (incase they dont know)
    show_instructions = yes_no("Would you like to see how to make a burger?")

    if show_instructions == "yes":
        print("A burger uses these main ingredients...\n")
    elif show_instructions == "no":
        print("sweet, lets make a burger! \n")

