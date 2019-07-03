# Simple program, but I don't have time to improve it
# Here's how I know to make it better:
def encodeTheWord(word):
    length = len(word)
    encoded = [None] * length
    encoded[0] = word[0]
    # This could probably be replaced via some function of n
    back_index = 1
    for n in range(1, length):
        # Who need's flags?
        if n % 2 == 0: 
            encoded[n] = word[back_index]
            back_index += 1
        else:
            encoded[n] = word[-back_index]
    # Idk why this is a thing? Perhaps a better implementation
    # this comes more naturally, and seems less like a gotcha
    # for not reading the assignment desc
    if length % 2 != 0:
        encoded.append(word[length//2])
    return ''.join(encoded)

def main():
    while True:
        word = input("Please enter a word (zzz to finish): ")
        # Allows for spaces
        if "zzz" in word: 
            break
        if len(word) < 4:
            print(f"The word cannot be processed as it is not at least for characters long\n")
        else:
            print(f"The original word is {word}")
            print(f"The encoded word is: {encodeTheWord(word)}\n")

main()
