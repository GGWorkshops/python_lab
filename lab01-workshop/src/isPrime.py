#!/usr/bin/env python3

# obonhamcarter@allegheny.edu
# date 3 Sept 2019

data = open("../input/dataFile.txt") # finds dataFile and creates data variable
numOfPrimes_int = 0
numOfNonPrimes_int = 0
numOfNums_int = 0


for line_str in data:
    #print( "line_str : ",line_str)
    numOfNums_int += 1 # how many numbers its already been through
    try: # if the line contains something other than an integer (convert string to int)
        n_int = int(line_str) # note: n_int is an integer
    except ValueError: # catch the non-integer
        pass

    isPrime = True

    # TO DO: Complete the program to check primality

    for i in range(2, n_int):
        if (n_int % i) == 0: #if the % is 0 than it is not prime
            isPrime = False
            numOfNonPrimes_int += 1
            break
    if(isPrime == True):
        numOfPrimes_int += 1




print("    Number of values in file   : ",numOfNums_int)
print("    Number of primes           : ",numOfPrimes_int)
print("    Number of composites        : ",numOfNonPrimes_int)
