#code to perform quick sorting technique

#Function to find the pivot index
def getPivot(li,first,last):
    pivot = li[first]
    left = first + 1
    right = last

    while True:
        while left <= right and li[left] <= pivot:
            left += 1
        while left <= right and li[right] >= pivot:
            right -= 1

        if right < left:
            break
        else:
            li[left],li[right] = li[right],li[left]

    li[first],li[right] = li[right],li[first] 
    return right

def quickSort(li,first,last):
    
    if first < last:
        p = getPivot(li,first,last)
        quickSort(li,first,p-1)
        quickSort(li,p+1,last)

#main
li = [56,26,93,17,31,44]
quickSort(li,0,len(li)-1)
print(li)