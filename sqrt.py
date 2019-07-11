n = float(input("input number to approximate square root"))
neg = False
if(n<0):
  n = -n
  neg = True
actualsqrt = n**0.5
nlen = len(str(int(n)))
if(n%2==0):
  old = 6*(10**((nlen-2)/2))
  print("Using " + str(old) + " as init guess")
else:
  old = 2*(10**((nlen-2)/2))
  print("Using " + str(old) + " as init guess")
new = 0.5*(old + (n/old))
numIter = 1
while(True):
  print("New = " + str(new))
  print()
  if((abs(((new*new)/n)-1))<=0.000000001):
    if(neg):
      print("Square root is: " + str(new) + "i")
    else:
      print("Square root is: " + str(new))
    print("Found in " + str(numIter) + " iterations")
    break
  print()
  old = new
  new = 0.5*(old + (n/old))
  numIter = numIter + 1
  print()
  

