
def bubble_sort(arr):
    n = len(arr) # Finding the length 
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def arm(num):
    if num%10==0:
        print("The given number is even")
    else:
        print("The given number is odd")
    
# Array creation
arr = [64, 34, 25, 12, 22, 11, 90]
# transfer into var
sortedarr = bubble_sort(arr)
#print
print(sortedarr)
arm(10)
