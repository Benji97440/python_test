#coding:utf-8
class numb:
    def __init__(self, x, y):
        self.a = x
        self.b = y
    def syracuse_numb(self):
        varia = self.a
        for i in range(1, self.b+1):
            if varia%2==0:
                varia = varia//2
            else:
                varia = 3*varia+1
        return b


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
multi = numb(34,32)
print(getlist(multi.syracuse_numb,32))



