#A program to create a dictionary to record the phone numbers


n=int(input("Enter the Name and Phone number: ))
d={}
for i in range(0,n):
	x=input().split()
	d[x[0]] = x[1]
print (d)
