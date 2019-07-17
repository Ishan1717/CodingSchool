class Stack():
  def __init__(self, array):
    #init stack using a starter array
    self.array = array
  def push(self, value):
    #adds value to end
    self.array.append(value)
  def pop(self, value):
    #creates temporary array to preserve elements, also sets original to 0
    temp = self.array
    self.array = []
    #puts all elements except the last one into the array
    for x in range (0,len(temp)-1):
      self.array.append(temp[x])
    #returns the last element of temp array
    return(temp[len(temp)-1])
class Queue():
  def __init__(self, array):
    self.array = array
  def push(self, value):
    self.array.append(value)
  def pop(self, value):
    temp = self.array
    self.array = []
    for x in range(1,len(temp)):
      self.array.append(temp[x])
    return(temp[0])
#Given a string of an even length, write a code that reverses the string, and that swaps the first half and second half of the string

string = "abcdef"
reverse = ""
for x in range(len(string)-1,-1,-1):
  reverse = reverse + string[x:x+1]
print("Reverse: " + reverse)

swap = ""
swap = swap + string[int(len(string)/2):int(len(string))] + string[int(0):int(len(string)/2)]
print("Swap: " + swap)




#Given an array/list of no less than 10 integers, return the sum of the first 2 elements in the array/list. If the length is less than 2, just sum up the elements that eist, and return 0 if the length is 0.
#Implement the following: a sorting algorithm, a reverse sorting algorithm, and return the number of even numbers in the array.
temp1 = 0
temp2 = 0

array = [1,3,5,7,9,2,4,6,8,10,19]

print(array[0]+array[1])

for y in range(0,len(array)):
  for x in range(0,len(array)-1):
    if(array[x]>array[x+1]):
      temp1 = array[x]
      temp2 = array[x+1]
      array[x+1] = temp1
      array[x] = temp2
print(array)

for y in range(0,len(array)):
  for x in range(0,len(array)-1):
    if(array[x]<array[x+1]):
      temp1 = array[x]
      temp2 = array[x+1]
      array[x+1] = temp1
      array[x] = temp2
print(array)

count = 0

for x in range(0,len(array)):
  if(array[x]%2==0):
    count = count + 1
print(count)



    list.append(''.join(sorted(string)))

  
def combination (p,s):
  if len(p) > 0:
    print (p)
  if len(s) == 0:
    return
  for i in range(0,len(s)):
    combination(p+s[i], s[i+1:])

T = int(input())
for l in range (0,T):
  N = int(input())
  S = input()
  combination ('',''.join(sorted(S)))
  
string = "{([]}"
leftParen = 0
rightParen = 0
leftBracket = 0
rightBracket = 0
leftCurly = 0
rightCurly = 0
for x in range(0,len(string)):
  if(string[x:x+1]=="("):
    leftParen = leftParen + 1
  elif(string[x:x+1]==")"):
    rightParen = rightParen + 1
  elif(string[x:x+1]=="["):
    leftBracket = leftBracket + 1
  elif(string[x:x+1]=="]"):
    rightBracket = rightBracket + 1
  elif(string[x:x+1]=="{"):
    leftCurly = leftCurly + 1
  elif(string[x:x+1]=="}"):
    rightCurly = rightCurly + 1
if(leftParen - rightParen == 0):
  if(leftBracket-rightBracket==0):
    if(leftCurly-rightCurly==0):
      print(True)
    else:
      print(False)
  else:
    print(False)
else:
  print(False)
  
curlystack = []
roundstack = []
hardstack = []

if ('{'):
  curlystack.append()


if ('}')
  curlystack.pop()

if !curlystack.peep()

string = "qwrrwq"
list = []




#insert the string into the list
for x in range(0,len(string)):
  list.insert(0,string[int(x)])
newString = ""
#go back through the list by popping and check if the new strign is the same as the old one
for x in range(0,len(string)):
  newString = list.pop() + newString
if(string == newString):
  print(True)
else:
  print(False)

