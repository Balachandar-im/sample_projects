class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

a = Add(2,3)
print(a.add())


class Multiadd(Add):
    def __init__(self,a,b,*args):
        super().__init__(a,b)
        self.args = args

    def mult_add(self):
        return sum((self.a,self.b) + self.args)

f = Multiadd(5,5,10,20,10)
print(f.mult_add())