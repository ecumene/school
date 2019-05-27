itemA = int(input("Please enter the number of ItemA sold: "))
itemB = int(input("Please enter the number of ItemB sold: "))
itemC = int(input("Please enter the number of ItemC sold: "))

print("The selling price of ItemA is $27.50")

print("The selling price of ItemB is $60.50")

print("The selling price of ItemC is $115.00")

price1 = (itemA * 25 + itemB * 55 + itemC * 100)
price2 = (itemA * 27.5 + itemB * 60.5 + itemC * 115)

print(f"Total Cost to Produce (all items sold) is ${price1}")

print(f"Total Sales (all items sold) is ${price2}")

print(f"Profit is ${price2-price1}")

total_sold = itemA + itemB + itemC

print(f"Percentage of ItemA sold is %{itemA / total_sold * 100.0}")

print(f"Percentage of ItemA sold is %{itemB / total_sold * 100.0}")

print(f"Percentage of ItemA sold is %{itemC / total_sold * 100.0}")
