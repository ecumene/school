# Is it in the range of numbers?
def shouldProcess(n):
    return n in range(6, 13) # 13 = 12 + 1 :)

# Pretty simple, add all in range
def findSum(n):
    # Has to be at least 6, so lets skip 1-5
    sum = 21
    for i in range(7, n+1):
        sum += i
    return sum

def findDivisors(n):
    # return i in range of:
    # MIN: 2              - Skip one, as per assignment
    # MAX: n + 1 // 2 + 1 - We only need to check half of them 
    # The last two are to check if it is divisible and if it isn't the n/n case
    return [i for i in range(2, (n + 1) // 2 + 1) if n % i == 0 and n != i]

# Very simple here
def processInput(n):
    if(shouldProcess(n)):
        sum = findSum(n)
        print(f"The sum from 1 to {n} is: {sum}")
        print(f"The divisors of {sum} are:")
        for x in findDivisors(sum):
            print(x, end = ' ')
        print()
    else: 
        print(f"The number {n} is outside of the acceptable range.")

def main():
    number = int(input("Please enter an integer between 6 and 12, inclusive: "))
    processInput(number)

main()
