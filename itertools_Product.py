a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in a:
    for j in b:
        print((i,j),end=' ')

# I can also use list comprehension 
# certasiann product=[(i,j)for j in b for i in a]     



# I could also use product method
# print(list(product(a,b)))   