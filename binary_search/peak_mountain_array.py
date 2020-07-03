"""Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that
 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, 
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]."""

arr = [0,1,3,1,0]

def peakIndexInMountainArray(arr):
    start, end = 0, len(arr) -1
    mid = (start + end ) // 2
    print(mid)

    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    
    elif arr[mid] < arr[mid - 1]:
        end = mid - 1
    
    elif arr[mid] > arr[mid + 1]:
        start = mid + 1
    
    return start

print(peakIndexInMountainArray(arr))
    