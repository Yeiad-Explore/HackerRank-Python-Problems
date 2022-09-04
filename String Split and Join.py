# a =  'hello world, Im kabid yeiad'

# b = a.split(" ")
# c = '-'.join(b)

# print(c)

# a = input().split()

# b = '-'.join(a)

# print(b)

def split_and_join(line):
    
   a = line.split()
   x ='-'.join(a)
   return x
    
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)