n = int(input())
x = {}

for i in range(n):
    name , *line = input().split()
    scores = list(map(float, line)) 
    x.update({name:scores})
query = input()
marks = x[query]
y = format(sum(marks)/len(marks),'.2f')
print(y)