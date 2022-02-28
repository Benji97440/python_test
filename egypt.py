def Egypt(a,b):
	A = a
	B = b
	temp = 0
	while A!=0:
		if A%2 == 1:
			temp += B
		A = A//2
		B *= 2
	return(temp)

print(Egypt(34,32))