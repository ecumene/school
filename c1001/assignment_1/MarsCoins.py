import math

maruvian_to_paruvian = 24
maruvian_to_taruvian = 4
maruvian_to_caruvian = 2

prompt = "Please enter the number of "

maruvians = int(input(f"{prompt} Maruvians: "))
maruvians += int(input(f"{prompt} Caruvians: ")) / maruvian_to_caruvian
maruvians += int(input(f"{prompt} Taruvians: ")) / maruvian_to_taruvian
maruvians += int(input(f"{prompt} Paruvians: ")) / maruvian_to_paruvian
sharees = int(input("Please enter the number of friends: ")) + 1

maruvians_floor = math.floor(maruvians)

print(f"Marvin has {maruvians_floor} Maruvian(s) in total.")

print(f"He gives {math.floor(maruvians / sharees)} Maruvian(s) to himself and "
      + f"to each of his {sharees - 1} friends.")

print(f"Marvin puts back {math.floor(maruvians % sharees)} Maruvian(s) and "
      + f"{math.ceil((maruvians - maruvians_floor) * maruvian_to_paruvian)}"
      + " Paruvian(s) back in the jar.")
