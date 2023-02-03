#code to perform merge sort

def mergeSort(list1):
    
    if len(list1) > 1:
        mid = len(list1) // 2
        leftList = list1[ :mid]
        rightList = list1[mid: ]
        mergeSort(leftList)
        mergeSort(rightList)
    
        i = j = k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] <= rightList[j]:
                list1[k] = leftList[i]
                i += 1
                k += 1
            else:
                list1[k] = rightList[j]
                j += 1
                k += 1
        
        while i < len(leftList):
            list1[k] = leftList[i]
            i += 1
            k += 1
        
        while j < len(rightList):
            list1[k] = rightList[j]
            j += 1
            k += 1 

list1 = [10,2,5,1,9,2]
mergeSort(list1)
print(list1)