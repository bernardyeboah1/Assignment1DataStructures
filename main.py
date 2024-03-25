def mergeSort(arr):
    if len(arr) > 1:
        leftArray = arr[:len(arr)//2]
        rightArray = arr[len(arr)//2:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1

        print(arr)

productID = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
mergeSort(productID)
print(productID)





    




