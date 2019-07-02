#Overall function that when called actually executes the calculator. This calculator should display a list of options to the user: whether they want to add, multiply, divide, substract a set of numbers. Additionally, the user should have the options to exponentiate a number, take a number to an nth root, or quit the calculator. Each of these options should consist of a different function.

#Requirements for Add/Subtract/Mult/Divide: take in the number of numbers the user wants to calculate, than take in each number. Display the result as follows to the user: [n1] [mathematical operator] [n2] [operator] ... [nf] = [result]

##Exponentiation and nth roots should only take in two numbers

##Quitting should terminate the program

#Once any option other than quitting is complete, ask the user if they would like to continue or quit. If the user chooses to continue, restart the calculator. Otherwise, call your quit function
def calc():
  inp = input("Select a function:  add, subtract, multiply, divide, exponent, root, or quit")
  while(True):
    if(inp == "add"):
      add()
    elif(inp=="subtract"):
      subtract()
    elif(inp=="multiply"):
      multiply()
    elif(inp=="divide"):
      divide()
    elif(inp=="exponent"):
      exponent()
    elif(inp=="root"):
      root()
    elif(inp=="quit"):
      break
    else:
      print("Please input valid command")
    inp = input("Select a function:  add, subtract, multiply, divide, exponent, root, or quit")


def add():
  n = int(input("How many addends?"))
  total = 0
  final = ""
  for x in range(0,n):
    a = int(input("Type number: "))
    final = final + (str(a) + " + ")
    total = total + a
  final = final[0:(int(len(final))-2)] + "= " + str(total)
  print(final)

def subtract():
  n = int(input("How many numbers?"))
  a = int(input("Type number: "))
  total = a
  final = str(a) + " - "
  for x in range(0,n-1):
    a = int(input("Type number: "))
    final = final + (str(a) + " - ")
    total = total - a
  final = final[0:len(final)-2] + "= " + str(total)
  print(final)

def multiply():
  n = int(input("How many multiplicands?"))
  total = 1
  final = ""
  for x in range(0,n):
    a = int(input("Type number: "))
    final = final + (str(a) + " * ")
    total = total * a
  final = final[0:(int(len(final))-2)] + "= " + str(total)
  print(final)

def divide():
  n = int(input("How many dividends?"))
  a = int(input("Type number: "))
  total = a
  final = str(a) + " / "
  for x in range(0,n-1):
    a = int(input("Type number: "))
    final = final + (str(a) + " / ")
    total = total / a
  final = final[0:len(final)-2] + "= " + str(total)
  print(final)

def exponent():
  a = input("Input base: ")
  b = input("Input exponent: ")
  print(str(a) + "^" + str(b) + " = " + str(int(a)**int(b)))

def root():
  a = input("Input number to be rooted: ")
  b = input("Input degree of root: ")
  print("sqrt_" + str(b) + "(" + str(a) + ") = " + str(int(a)**(1.0/int(b))))
calc()


  
