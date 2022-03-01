#coding:utf-8
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
contenu  = fichier.readline()
a = contenu[0]
b = contenu[1]
fichier.close()
print(getlist(a,b))
