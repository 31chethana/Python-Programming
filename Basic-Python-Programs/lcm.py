def lcm(num1, num2):
  if num1 > num2:
      max = num1
  else:
      max = num2
  while(True):
      if ((max % num1 == 0) and (max % num2 == 0)):   
          lcm=max
          break
      max= max+ 1
  return lcm



x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
print "The lcm of ",x," and ",y," is ",lcm(x,y)

