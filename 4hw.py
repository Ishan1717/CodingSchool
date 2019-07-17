def findCombos(length):
  if(length==3):
    return(findCombos(length-2) + 1 + findCombos(length-1))
  elif(length==2):
    return(findCombos(length-1) + 1)
  elif(length==1):
    return(1)
  elif(length<1):
    return(0)
  else:
    return(findCombos(length-3) + findCombos(length-2) + findCombos(length-1) + 3)  
print(findCombos(7))
