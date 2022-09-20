s = input()

alnum = False
alpha = False
digt = False
low = False
up = False

for i in s:
   if i.isalnum():
    alnum = True
   if i.isalpha():
    alpha = True 
   if i.isdigit():
    digt = True 
   if i.islower():
    low = True
   if i.isupper():
    up = True  
print(alnum)
print(alpha)    
print(digt)
print(low)
print(up)

