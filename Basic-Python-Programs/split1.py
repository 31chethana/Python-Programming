#Example for split() function in python

a,b,c=input("Enter 3 numbers: ").split()
print(a,"  ",b,"  ",c)

#code enter n numbers using split() and print it in reverse order.
n=int(input())
A=input().split()
print(A)
k=n-1
for i in range(0,n):
	print(A[k],end=" ")
	k=k-1


