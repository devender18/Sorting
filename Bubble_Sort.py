#code to perform bubble sort
li = [10,115,4,23,0,89,23,21.40,53]

for i in range(len(li)-1):
    for j in range(len(li)-li-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1],li[j]

print(li)
