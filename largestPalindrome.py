#
# Finds the largest palindrome for each number of digits specified
# Time complexity: O(n^2)
#

import math, time
    
def largestPalindrome(digits):
    largest = 0

    num = pow(10,digits) - 1

    duplicate = num 

    for i in range(num, int(num*.91), -1): #check top 9% of numbers
        for j in range(duplicate, int(num*.91), -1): #check top 9% of numbers, never check duplicates
            product = str(i*j)
            prodDigits = len(product)
            #if prodDigits < digits*2: #saving time...may not be doing anything anymore
            #    break
            firstHalf = product[:prodDigits//2]
            secondHalf = product[prodDigits//2:]
            secondHalf = secondHalf[::-1] #flip
            
            if (firstHalf == secondHalf):
                if (i*j) > largest:
                    largest = (i*j)
            #print("i", i, "j", j, "product:", product, "firstHalf:", firstHalf, "secondHalf flipped:", secondHalf, "largest:", largest)
        duplicate -=1 #saving time by not checking duplicates

    return largest

def main():
    digits = 5	#Modify this value
    print("Digits:", digits)
    print("Running...")
    start = time.time()
    result = largestPalindrome(digits)
    end = time.time()
    print("Largest", digits, "digit palindrome:", result)
    if (end - start) > 60:
        print("Time elapsed: ", (end - start)/60, "minutes")
    else: 
        print("Time elapsed: ", end - start, "seconds")

main()