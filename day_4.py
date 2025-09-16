class operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        ad=self.a+self.b
        return ad
    def mul(self,a,b):
        ml=self.a*self.b
        return ml
    def div(self,a,b):
        div=self.a/self.b
        return div
    def sub(self,a,b):
        sb=self.a-self.b
        return sb
    
oj=operations(10,10)
print("addition is",oj.add())



class operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def vowels(self):
        count=0
        v=['a','e','i','o','u']
        for char in self.a:
            if char in v:
                count+=1
        print("the number of vowels is",count)
    def vowels_ind(self):
        count=0
        d={}
        v=['a','e','i','o','u']
        for char in self.b:
            if char in v:
                d[char]=d.get(char,0)+1
        print("The each occurance of the word",d)

    def count_list(self):
        c=self.a+self.b
        print("The total lenght of two list is",len(c))

    def small_num(self):
        small=self.a[0]
        for i in range(1,len(a)):
            if self.a[i]<small:
                small=self.a[i]
        print("the smallest number is ",small)

a="appi"
b="adgkl"
obj=operations(a,b)
obj.vowels()
obj.vowels_ind()
obj.count_list()
c=[1,2,3,4,5]
obj1=operations(c,None)
obj1.small_num()



    