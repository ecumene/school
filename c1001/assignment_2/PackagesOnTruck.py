limit = int(input("Please enter the weight limit of the truck: "))

# This makes looking up to add to zones easy
# and showing all outbound directions as well
zones = {
    'East': 0,
    'West': 0,
    'North': 0,
    'South': 0
}

on_truck = 0
packages_on_truck = 0
while True:
    # Description had float values
    pkg_weight = float(input("\nPlease enter the weight of a package: ")) 
    # If it's going to be more than the truck can take, break
    if on_truck + pkg_weight > limit:
        break
    pkg_number = int(input("Please enter the package ID number: ")) 
    pkg_zone = input("Please enter the zone: ")
    
    print("\nThe following package is on the truck:")
    print(f"Pkg No. = {pkg_number} , Zone = {pkg_zone} , Pkg wgt = {pkg_weight}")

    on_truck += pkg_weight
    # Lookup the given zone in the dictionary, add one
    zones[pkg_zone] += 1
    packages_on_truck += 1

print()

# Print all zones and the content
for zone, packages in zones.items():
    print(f"{packages} are on the truck for the {zone} zone.")

print(f"\n{packages_on_truck} packages are loaded on the truck.")