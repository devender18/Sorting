#Selection sorting
li = [45,24,9,65,11,29,6,10]
for i in range(len(li)):
    minVal = min(li[i:])
    minValIndex = li.index(minVal,i)
    li[i],li[minValIndex] = li[minValIndex],li[i]

print(li)