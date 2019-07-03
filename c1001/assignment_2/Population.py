municipalities = int(input("Please enter the number of municipalities: "))

# Tuple structs because names and populations are pairs
highest = (0, "")
# There isn't 10,000,000,000,000 people in the world
# sys.maxsize could also be used here, but I like to avoid imports
lowest = (10000, "") 
avg = 0

for n in range(municipalities):
    name = input("Enter the municipality: ")
    popu = float(input("Enter the population: "))

    if popu > highest[0]:
        highest = (popu, name)
    # Lowest starts high, so we can't miss it
    if popu < lowest[0]:
        lowest = (popu, name)

    # Avg = sum of all over elements
    # This is the same thing (division distributes)
    avg += popu / municipalities

# f strings are a beautiful thing

print(f"The municipality with the highest population of {highest[0]} million was {highest[1]}")
print(f"The municipality with the lowest population of {lowest[0]} million was {lowest[1]}")
print(f"The range of population amounts for the {municipalities} municipalities was {highest[0] - lowest[0]}")
print(f"The average population amount for the {municipalities} municipalities is {round(avg, 2)}")
