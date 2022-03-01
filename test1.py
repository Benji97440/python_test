#coding:utf-8
class numb:
    def __init__(self, x, y):
        self.a = x
        self.b = y
    def syracuse_numb(self,j):
        c = self.a
        for i in range(1,j+1):
            if c%2==0:
                c = c//2
            else:
                c = 3*c+1
        return c

    def getlist(self,x,n):
        L = []
        mul = numb(x,n)
        for j in range(n):
            L = L+[mul.syracuse_numb(j)]
        return L

multi = numb(12,20)
print(multi.getlist(12,20))