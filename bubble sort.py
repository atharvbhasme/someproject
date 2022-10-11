lst=[]
n=int(input())
swapped=True
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
while swapped:
    swapped=False
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            swapped=True
            lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)
