def findCombos(length):
  if(length==3):
    return(findCombos(length-2) + findCombos(length-1) + 1)
  elif(length==2):
    return(findCombos(length-1)+1)
  elif(length==1):
    return(1)
  elif(length<1):
    return(0)
  else:
    return(findCombos(length-3) + findCombos(length-2) + findCombos(length-1))  
print(findCombos(7))


n = int(input("Enter number of queries"))
dict = {}
for x in range(0,n):
  name = input("Enter name")
  number = input('Enter phone number')
  dict[name] = number
while(True):
  query = input()
  if(query not in dict):
    print("Not found")
  else:
    print(dict[query])
    
    
dict = {}
temp = input("Enter sentence in magazine")
array = temp.split(" ")
i=0
for x in array:
  dict[i]=x
  i=i+1
print(dict)
check = True


temp = input("Enter sentence in note")
array = temp.split(" ")
print(array)

for x in array:
  check2 = False
  for y in dict:
    if(dict[y]==x):
      check2 = True
      del dict[y]
      break
  if(not check2):
    check = False
if(check):
  print("Yes")
else:
  print("No")
  
a = set('abracadabra')
b = set('alakazam')
print(a ^ b)

# a - b letters in a but not b
#a | b letters in a or b or both
#a & b letters in both a and b
#a ^ b letters either in a or b but not both



plantset = set()
n = input("Enter number of plants")
array = input("Enter plant heights: ").split(" ")
sum = 0
numelements = 0
for x in array:
  plantset.add(int(x))
for x in plantset:
  sum = sum + x
  numelements = numelements + 1
print(sum/numelements)


roomset = set()
roomlist = input().split(" ")
for x in range(0,len(roomlist)):
  roomset.add(roomlist[x])
roomsetcopy = list(roomset)
for x in roomset:
  for y in roomlist:
    if(x==y):
      temp = x
      roomsetcopy.remove(x)
      roomlist.remove(y)
      break

for x in roomset:
  if(x not in roomlist):
    print(x)
    break
