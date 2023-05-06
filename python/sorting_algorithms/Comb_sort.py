def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        i = 0
        swapped = False
        while i + gap < n:
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                swapped = True
            i += 1
    return arr

arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(comb_sort(arr))
    if comb_sort(arr)[2]%10==0:
        print("The second index of array is even")
    else:
        print("The second index of array is odd")