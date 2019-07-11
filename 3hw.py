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
    for x in range (0,temp.len-1):
      self.array.append(temp[x])
    #returns the last element of temp array
    return(temp[len(temp)-1])
  
  
