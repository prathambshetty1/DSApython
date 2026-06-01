start=[1,3,0,5,8,5]
finish=[2,4,6,7,9,9]
print("Selected Activities: ")
i=0
print(i)
for j in range(1,len(start)):
    if start[j]>=finish[i]:
        print(j)
        i=j