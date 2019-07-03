# Returns the nearest multiple of three *rounding up*
def nearest_of_three(x):
    # No ceil function, no problem :)
    # The only case round rounds down, is if 1 is 
    # the remainder, so we fix that
    if x % 3 == 1:
        x += 1
    return 3 * round(x/3)

# This is pretty simple, multiply the number above by three
def findThird(section_height):
    return nearest_of_three(section_height) / 3

# Prints top and bottom section of the H
def printTopAndBottom(section_height):
    for i in range(section_height):
        # Multiplying strings expands to repeated append
        print("h" * section_height
              + " " * section_height 
              + "h" * section_height)

def printMidH(section_height):
    for i in range(section_height):
        print("h" * section_height * 3)

def main():
    height = int(findThird(int(input("Please enter the height of H: "))))
    printTopAndBottom(height)
    printMidH(height)
    printTopAndBottom(height)

# If you like ascii art, you should check out this thing I made
# https://ecumene.xyz/posts/sloth/
main()
