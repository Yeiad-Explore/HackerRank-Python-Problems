n = int(input())
result = []
grade = []
names = []
for i in range(n):
    name =  input()
    marks = float(input())   
    result.append([name,marks])          
    grade.append(marks) 
grade = sorted(set(grade)) 
x = grade[1] 
for j in result:
    if x == j[1]: 
        names.append(j[0])

names= sorted(names)        
for k in names:
    print(k)


