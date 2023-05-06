def gnome_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr


arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(gnome_sort(arr))
    if gnome_sort(arr)[2]%10==0:
        print("The second index of array is even")
    else:
        print("The second index of array is odd")