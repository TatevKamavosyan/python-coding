class X:
    def val(self):
        return 3
    
class Y(X):
    def val(self):
        return super().val() * 2

y=Y()
print(y.val())       

