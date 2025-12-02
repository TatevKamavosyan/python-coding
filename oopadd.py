class Alpha:
    def __init__(self,a):
        self.__a=a


    def __add__(self, other):

        return Alpha(self.__a - other.__a)
    
x= Alpha(10)
y= Alpha(4)    
z= x + y
print(type(z))