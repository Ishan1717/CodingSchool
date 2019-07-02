##Test if a number chosen by the user is in the Fibonacci sequence. If it is NOT part of the sequence, report the closest number that is. If it is, tell the user it is part of the sequence.

a = 0
b = 1
check = True
alternate = True
num = int(input("select a number"))
while(check):
  if(num<a or num<b):
    if(abs(num-a) < abs(num-b)):
      print("Closest number is " + str(a))
    else:
      print("Closest number is " + str(b))
    check = False
  elif((num==a) or (num==b)):
    print("Your number is a fibonacci number")
    check = False
  else:
    if(alternate):
      a = a + b
      alternate = False
    else:
      b = b + a
      alternate = True
