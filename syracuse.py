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

def syracuse(x,n):
    b = x
    for i in range(1, n+1):
        if b%2==0:
            b = b//2
        else:
            b = 3*b+1
    return b

def getlist(x, n):
    L = []
    for j in range(n):
        L = L+[syracuse(x, j)]
    return L


fichier = open('syracuse.txt', 'r')
a = int(fichier.readline())
b = int(fichier.readline())
print(a,b)
fichier.close()
print(getlist(a,b))

multi = numb(12,20)
print(multi.getlist(12,20))



