def bubble_sort(arr):
    length = len(arr)

    for j in range(length):
        for i in range(length-1):
            if arr[i] < a[i+1]:
                arr[i] , a[i+1] = a[i+1],arr[i]

if __name__ == "__main__":
    a = [10, 3, -3, 6, 0, 1, 4, 5, 11, 8,10,-10]
    bubble_sort(a)
    print(a)