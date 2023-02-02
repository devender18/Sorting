# Code to perform insertion sorting
li = [43,12,5,24,64,2,5]

for i in range(1,len(li)):
    currVal = li[i]
    pos = i

    while pos > 0 and currVal < li[pos-1]:
        li[pos] = li[pos-1]
        pos -= 1
    li[pos] = currVal

print("After sorting:",li)