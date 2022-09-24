from random import randint
from re import I
import numpy as np

# a=[2,1,3,[1]]


# array1=[-2,-1,0,1,2,3]
# array1.sort()


# def change(arr,n):
#     for i in range(n-1,0,-1):
#         j=randint(0,i+1)
#         arr[i],arr[j]=arr[j],arr[i]
#         return arr
#     arr=[1,2,3]
#     n=len(arr)
#     print(change(arr,n))

 

arr = np.array([1, 2, 3])
 


 

np.random.shuffle(arr)
 


print(arr)


def sortSquare(arr, n):
 
   
    for i in range(n):
        arr[i]= arr[i] * arr[i]
    arr.sort()
 

arr = [ -3, -1, 0, 1, 2]
n = len(arr)
 

for i in range(n):
    print(arr[i], end = " ")
 

 
sortSquare(arr, n)
 

for i in range(n):
    print(arr[i], end = " ")
 