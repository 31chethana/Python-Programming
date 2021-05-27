#To convert decimal number into binary number
s=""
n=int(input())
while n>0:
	a=n%2
	s=s+str(a)
	n=n//2
	
for i in range(len(s)-1,-1,-1):
	print(s[i],end="")
	
print()

#To print number of consecutive one's in the binary equivalent
count=0
temp=0
for i in range(len(s)-1,-1,-1):
	if s[i]=='1':
		count=count+1
		if(temp<count):
			temp=count
	elif s[i]=='0':
		count=0
print(temp)























