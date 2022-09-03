lst=[]
N = int(input("Print a Num: "))

for i in range(N):
    a= input("Print Command: ").split()

    if a[0]=='insert': #insert command
        lst.insert(int(a[1]),int(a[2]))
    elif a[0] == 'print':
        print(lst)
    elif a[0] =='remove':
        lst.remove(int(a[1]))
    elif a[0] == 'append':
        lst.append(int(a[1]))
    elif a[0] == 'sort':
        lst.sort()  
    elif a[0] == 'pop':
        lst.pop()       
    elif a[0] == 'reverse':
        lst.reverse()
