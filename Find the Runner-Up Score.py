
n = int(input())
arr = list(map(int,input().split()))
#arr = list(arr)

a = max(arr)
c = arr.count(a)


for i in range(c):
     arr.remove(a)

print(max(arr))   

 