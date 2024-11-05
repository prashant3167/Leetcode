arr1 = [[1,1,2,3],[3,4,5],[6,7,8],[10,11,12]]
arr2 = [[1,2,3],[3,4,5, 13],[6,7,8, 11],[9,10,11,12]]

# output 3 13 and 9
# In arr2 

dict = {}

for i in arr1:
    for j in set(i):
        if j in dict:
            dict[j] +=1
        else:
            dict[j] = 1
ans = set()
for i in range(len(arr2)):
    if (i>0 and arr2[i-1][-1]>=arr2[i][0]):
        continue
    for j in set(arr2[i]):
        if j not in dict or dict.get(j, 0)>1:
            ans.add(j)
print(ans)fir