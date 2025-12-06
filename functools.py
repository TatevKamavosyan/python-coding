from functools import reduce

a=[5]
for i in range(3):
        
        print(reduce(lambda x, y: x * y, a))