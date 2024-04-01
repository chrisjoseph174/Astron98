#HW-5
import numpy as np

#Problem 1 - Hey Twin
#Given an array, find the rows where all the values are equal.

def findEqual(arr):
    emptyArray = []
    for row in arr:
        if np.all(row==row[0]):
            emptyArray.append(row)
    return emptyArray


#Problem 2 - Checkers
#Create an 8x8 array with a checkerboard pattern of zeros and ones using
#a slicing + striding approach.

def cBoard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2]=1 #Learned slicing from Quora
    board[1::2, 1::2]=1 #iluvQuora
    return board

print(cBoard())

#Problem 3 - I need some space
#Given an array of strings, return an array where each letter in each string is
#separated by a space.

def spaceBetween(myarr):
    return np.char.join(' ', myarr)

#Problem 4 - Everything is in order
#Given a multidimensional matrix, sort the matrix along the columns

def sort(randMatrix):
    return np.sort(randMatrix, axis=0)





