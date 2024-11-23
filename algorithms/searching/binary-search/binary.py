def binarySearch_IterativeApproach(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # Target not found


def binarySearch_RecursiveApproach(array, target, low, high):
    if low > high:
        return -1 # Target not found
  
    mid = (low + high) // 2

    if array[mid] == target:
        return mid 
    elif array[mid] < target:
        return binarySearch_RecursiveApproach(array, target, mid+1, high)
    else:
        return binarySearch_RecursiveApproach(array, target, low, mid-1)