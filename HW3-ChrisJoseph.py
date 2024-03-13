#Problem #1
#Write a function to compute the value of x raised to the power y without using the built-in pow or ** operator

def power(x,y):
    num = 1
    for i in range(y):
        num*=y
    return num

#Problem #2
#Write a function that takes a list of numbers as input and returns the minimum and maximum values in the list as a tuple.

def findMinMax(numbers):
    values = tuple()
    return values.append(min(numbers), max(numbers))

#Problem #3
#Write a function that takes a year as input and returns True if it’s a leap year, and False otherwise. 
#A leap year is divisible by 4 but not divisible by 100 unless it is also divisible by 400.

def isLeapYear(year):
    if year%4==0:
        return True
    if year%400==0:
        return True
    else:
        return False

#Problem #4
#Write a function that takes a person’s weight (in kilograms) and height (in meters) as input and returns their BMI.

def BMI(height, weight):
    if height<0:
        print("Height must be over 0.")
    return weight/(height**2)


#Problem 5
#Implement a function called rotate digits that takes an integer n as input and rotates its digits to the right by one position. For example, given the
#input 12345, the function should return 51234. You may *not* convert the input to a string but you can use properties of a string in your answer.
#Hint: Use modulus (%) and floor division (//).
#Ex: 12345 % 10 = 5 and 12345 // 10 = 1234

def rotateDigits(number):
    last = number % 10
    remaining = number // 10
    count = 1  

    while remaining > 0:
        remaining //= 10
        count += 1

    return (last * (10 ** (count - 1))) + remaining

#Problem 6
#For both minimum and maximum, write one function to manually find that value using a for loop and another to manually find it using a while loop. You
#may not use min() or max(). In total you should have written 4 functions.

def minForLoop(numbers):
    min_value = numbers[0]
    for smol in numbers:
         if smol < min_value:
            min_value = smol
    return min_value

def maxForLoop(numbers):
    max_value = numbers[0]
    for big in numbers:
        if big > max_value:
            max_value = big
    return max_value

def minWhileLoop(numbers):
    min_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1
    return min_value

def maxWhileLoop(numbers):
    max_value = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_value:
            max_value = numbers[i]
        i += 1
    return max_value
        
#Problem 7
#Write a function which takes in a string and outputs the number of vowels. Consider only a,e,i,o,u to be vowels and do not forget about capital letters.
#Ex: vowel count(”UC Berkeley”) will return 41

def vowels(word):
    count = 0
    for w in word:
        if 'a' in word.lower():
            count +=1
        if 'e' in word.lower():
            count +=1
        if 'i' in word.lower():
            count +=1
        if 'o' in word.lower():
            count +=1
        if 'u' in word.lower():
            count +=1
        if 'A' in word.lower():
            count +=1
        if 'E' in word.lower():
            count +=1
        if 'I' in word.lower():
            count +=1
        if 'O' in word.lower():
            count +=1
        if 'U' in word.lower():
            count +=1
    return count


#Problem 8
#Write a function that takes in an integer and returns the sum of the digits (the digital root). Ex: digital root(12345) will return 15

def digitalRoot(number):
    while number >= 10:
        total = 0
        while number > 0:
            total += n % 10
            number //= 10
        number = total
    return number

