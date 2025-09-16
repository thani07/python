class operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        ad=self.a+self.b
        return ad
    def mul(self):
        ml=self.a*self.b
        return ml
    def div(self):
        div=self.a/self.b
        return div
    def sub(self):
        sb=self.a-self.b
        return sb
    
oj=operations(10,10)
print("addition is",oj.add())