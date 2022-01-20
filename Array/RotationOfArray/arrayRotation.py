# Python Program for Array Rotation 
# Question Source : GFG 
# Author Akash Singh

# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 


# # Solution 1
# (Using temp array) 

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store the first d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]


def rotateArrayByN(arr,d):
    return arr[d:] + arr[:d]
      
print(rotateArrayByN([1,3,4,5,6,7], 2))



#  Solution 1
# (Rotate one by one)  

# leftRotate(arr[], d, n)
# start
#   For i = 0 to i < d
#     Left rotate all elements of arr[] by one
# end


def rotate(arr,d):
    for i in range(d):
        rotateByOne(arr)
    return arr
        
def rotateByOne(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp

print(rotate([1,3,4,5,6,7], 2))

