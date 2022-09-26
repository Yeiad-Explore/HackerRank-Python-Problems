
# # dict = {'USA':[10,20,30],'Bangladesh': [30,50,90]}

# # #value = dict.values() # for all values
# # value = dict["USA"] #for single values


# # print(f'Values of USA:{value} ')

# # updt= dict.update({'USA':[0,0,0]})
# # value = dict['USA']
# # print(f'Updated Values od USA : { value } ',)

# # new_dictionary = [('Micheal', 678), ('John', 987), ('John', 345), ('Oliva', 432), ('William', 445)]

# # empty_dictionary = {}
# # for i in new_dictionary:
# #     empty_dictionary.setdefault(i[0],[]).append(i[1])
# # print(empty_dictionary)

# # a = {}
# # b=[]
# # n = int(input("Enter Elements : "))

# # for i in range(n):
# #     key = input('Key: ')
# #     Value = input('Values:')
# #     a.update({key:Value})
# # print(a)    


# lst = [1,4,3,2,5,6,9,3,14]
# a = ['insert','5','10']

# lst.insert(int(a[1]),int(a[2])) #insert(index,object)
# print(lst)
# lst.sort()
# # lst.pop()
# # lst.reverse()
# lst.remove(lst[1])

# print(lst)
# s = 'hello'
# for i in range(0, len(s)):
#     print (s[i])

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))        
#     #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))   

#     #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))