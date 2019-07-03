# Keep going until break
while True:
    # Get the word
    word = input("Please enter a word (zzz to exit): ")
    
    # Check if we should break
    if word == "zzz":
        break

    print(f"The original word is {word}")
    
    # Break up the word into a list
    word = list(word)
    
    # This could also be done with REGEX-replace or join()
    # Enumerate so we can mutate the list
    for i, character in enumerate(word):
        if character.lower() in 'aeiou':
            word[i] = '*'
    
    # Join the list with nothing in between
    word = ''.join(word)
    
    print(f"The word without vowels is {word} \n")
