import random

def initializeList(randomNumbers): # Mutates randomNumbers
    for i in range(50): # 50 numbers
        randomNumbers.append(random.randint(1,50)) # add to list

def freqCount(frequency, randomNumbers):
    for i in randomNumbers: 
        # This could also be done with sum(1 for x in y if lower < r and r < upper) 
        # but this is faster with more code
        if(i < 11):
            frequency[0] += 1
        elif(i < 21):
            frequency[1] += 1
        elif(i < 31):
            frequency[2] += 1
        elif(i < 41):
            frequency[3] += 1
        elif(i < 51):
            frequency[4] += 1

def main():
    frequency = [0,0,0,0,0]
    randNumbers = []
    initializeList(randNumbers)
    freqCount(frequency, randNumbers)
    print(f"List of random numbers:\n{randNumbers}\n") # print numbers
    print(f"List of frequency counts:\n{frequency}\n") # print frequency
    printHistogram(frequency)                          # print histogram
    
def printHistogram(frequency):
    print(f"A histogram of frequency counts:\n")
    print(f" 1 - 10: {'*'*frequency[0]}") # multiply asterisk by frequency
    print(f"11 - 20: {'*'*frequency[1]}")
    print(f"21 - 30: {'*'*frequency[2]}")
    print(f"31 - 40: {'*'*frequency[3]}")
    print(f"41 - 50: {'*'*frequency[4]}")

main()
