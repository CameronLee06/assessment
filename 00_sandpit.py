import pandas

all_fruit = []
all_mains = []
all_prices = []

lunch_dict = {
    "Fruit": all_fruit,
    "Mains": all_mains,
    "Price": all_prices,
}

while True:
    fruit = input("Fruit: ")

    if fruit == "xxx":
        break

    mains = input("Mains: ")
    price = float(input("Price: "))

    # GST = price / 1.15

    # add content to lists!!
    all_fruit.append(fruit)
    all_mains.append(mains)
    all_prices.append(price)
    # all_GST.append(GST)


# make the panda..
lunch_panda_frame = pandas.DataFrame(lunch_dict)

lunch_panda_frame['GST By Miss'] = \
    lunch_panda_frame['Price'] / 1.15

print(lunch_panda_frame)