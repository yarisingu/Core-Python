def cycle_sort(arr):
    n = len(arr)
    for cycle_start in range(n-1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start+1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start+1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
    return arr



arr = [64,33,22,11,88,55]
if len(arr)==1 or len(arr)==2:
    print("please give more than two values")
else:
    print(cycle_sort(arr))
    if cycle_sort(arr)[2]%10==0:
        print("The second index of array is even")
    else:
        print("The second index of array is odd")

