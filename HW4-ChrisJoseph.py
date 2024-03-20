import numpy as np

#2.1 : 
#Create a variable (name it anything you want but make it descriptive!) that is assigned to a list 
#with the numbers 0 to 50. You should not have to write each number manually

list = [0,50]

#2.2
#Create a function that takes in a list and squares each element in the list 

def squareList(list):
    np.square(list)
    return list

#2.3
#You are given two lists: listA and listB. listA contains the integers 1 through
#10 while listB contains the integers 20 through 30. Return a single, new list
#containing only the odd integers of both lists in sorted order

listA = [1,11]
listB = [20,31]

def oddSort(listA, listB):
    listC = listA + listB
    oddList = []
    for num in listC:
        if (num % 2 != 0):
            oddList.append(num)
    return oddList

#3
#Using nested for loops, create and print a 5x5 2D list with the numbers 1 to 25
matrix = []

# Populate the matrix with numbers from 1 to 25
num = 1
for i in range(5):
    row = []  # Initialize an empty row for each iteration
    for j in range(5):
        row.append(num)
        num += 1
    matrix.append(row)

#3.2
#Now with your completed 2D list, replace all multiples of 3 with ’ ?’ character and print the resulting list

for i in range(5):
    for j in range(5):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] = '?'

#4
#Write a function that takes in a list and returns a copy of that list with duplicate values removed

def remove_duplicates(dupliList):
    cleanList = []
    seen = set()  # To keep track of seen elements

    for num in dupliList:
        if num not in seen:
            cleanList.append(num)
            seen.add(num)
    return cleanList

            
