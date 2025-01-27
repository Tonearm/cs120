from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits


def radixSort(U, b, A):
    k = math.ceil(math.log(U, b))
    n = len(A)
    V, K, ans = [], [], []
    
    for (i, _) in A:
        V.append(BC(i, b, k))
            
    for i in range (n):
        K.append((0, (A[i][1], V[i])))
    
    for j in range (k):
        counter = 0
        for (x, (y, z)) in K:
            K[counter] = (z[j], (y, z))
            counter += 1
                   
        K = countSort(b, K)
            
    for (x, (y, z)) in K:
        resum = 0
        for j in range (k):
            resum += z[j] * math.pow(b, j)
        ans.append((resum, y))
    
    return ans

def getTiming(U, b, A):
    timelist = []
    start = time.time()
    for i in range (10):
        mergeSort(A)
    end = time.time()
    timelist.append((end - start)/10)
    
    start = time.time()
    for i in range (10):
        countSort(U + 1, A)
    end = time.time()
    timelist.append((end - start)/10)
    
    start = time.time()
    for i in range (10):
        radixSort(U + 1, b, A)
    end = time.time()
    timelist.append((end - start)/10)
    
    return timelist
    
def getData():
    result = []
    
    for npow in range (1, 16):
        for Upow in range (1, 21):
            A = []
            n = 2 ** npow
            U = 2 ** Upow
        
            for i in range (n):
                A.append((random.randint(1, U), i))
                
            result.append((n, U, getTiming(U, n, A)))
            print(npow, Upow)
    
    print(result)
    return result
 
getData()    
        
                     
                     
                     