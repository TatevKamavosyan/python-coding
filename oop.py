class Num():
    def __init__(self,x):
        self.x = x

    def __truediv__(self, other):
        return Num(self.x+other.x)

n1 = Num(5)
n2 = Num(2)

print((n1 / n2).x )
