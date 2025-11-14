"""
Find Mininmum and Maximum calue from Array
"""

import array


# Find Minimum value in Unsorted array
def getMin(arr):
    minVal = arr[0]
    for n in arr:
        if n < minVal:
            minVal = n

    return minVal


arr = array.array("i", [45, 67, 32, 12, 9, 47, 78])
print("Minimum Value")
print(getMin(arr))

## Find the minimum Value along with the index
def getMinValInd(arr):
    minIndex = 0
    for n in range(len(arr)):
        if(arr[minIndex] > arr[n]):
            minIndex = n
    print(f"Minimum Index: {minIndex} and Minimum Value: {arr[minIndex]}")

getMinValInd(arr)    

## Get both Minimum and maximum vale of array
def getMinMax(arr):
    minIndex = 0
    maxIndex = 0
    for n in range(len(arr)):
        if arr[minIndex] > arr[n]:
            minIndex = n
        if arr[maxIndex] < arr[n]:
            maxIndex = n
    print(f"The minimum Index is {minIndex} and the minimum value is {arr[minIndex]}")
    print(f"The maximum Index is {maxIndex} and the maximum value is  {arr[maxIndex]}")
    
getMinMax(arr)
