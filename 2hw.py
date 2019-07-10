import random

###Create a text-based RPG combat program that allows choose a type of character and fight an enemy with a random character-type
#Program should greet user, show them the types of characters available along with their stats (or a brief description of them, your choice), and then prompt them to select one.
  #At least four different classes should exist with a general "Character" superclass.
#At this point, program should create an instance of the selected character as well as randomly-generated enemy for the player to fight.
  #random.uniform(0,1)

#The program then enters the combat phase.
#The player should be allowed to either Fight, Use a Skill (these skills may be made at your discretion), or to Defend. An attribute, speed, should determine who moves first.
#This continues until either the HP of the player or the enemy becomes equal to or less than 0, at which point a message indicating the result is immediately printed and the user is prompted to indicate whether they'd like to fight the same enemey, fight a different one,  choose a different class, or quit. 
#THe enemy will need to have some sort of discernment of how to act. The conditions on how an enemy chooses an act is up to you! One parameter: enemy should at least in part make a decision based on the last round.
class Character:
  def init(self):
    self.maxHp = 10
    self.hp = 10
    self.defense = 10
    self.atk = 10
    self.speed = 10
    self.usedSpecial = False
  def attack(self, char):
    char.hp = char.hp - self.atk + defense
  def printStats(self):
    print("HP: " + self.hp + " / " + self.maxHp)
    print("ATK: " + self.atk)
    print("DEF: " + self.defense)
  def defend(self):
    self.defense = self.defense + 5
  

class Knight(Character):
  def init(self):
    super().init()
    self.maxHp = 60
    self.hp = 60
    self.defense = 9
    self.atk = 10
    self.speed = 2
    self.usedSpecial = False
  def attack(self, char):
    super().attack(char)
    self.usedSpecial = False
    self.defense = 9
  def skill(self):
    if(self.usedSpecial == False):
      print("You block all damage this turn!")
      self.usedSpecial = True
      self.defense = 100
    else:
      print("You are too tired to use your special.")
  def printStats(self):
    super().printStats()
  def defend(self):
    super().defend()

class Mage(Character):
  def init(self):
    super().init()
    self.maxHp = 40
    self.hp = 35
    self.defense = 3
    self.atk = 17
    self.speed = 3
  def attack(self, char):
    super().attack(char)
    self.usedSpecial == False
  def skill(self):
    if(self.usedSpecial == False):
      print("Your attack is raised by 6!")
      self.usedSpecial = True
      self.atk = 23
    else:
      print("You are too tired to use your special.")
  def printStats(self):
    super().printStats()
  def defend(self):
    super().defend()
  

class Berserker(Character):
  def init(self):
    super().init()
    self.maxHp = 75
    self.hp = 75
    self.defense = 0
    self.atk = 12
    self.speed = 1
  def attack(self, char):
    super().attack(char)
    self.usedSpecial = False
  def skill(self):
    if(self.usedSpecial == False):
      print("You heal 8 hp!")
      self.usedSpecial = True
      self.hp = self.hp + 8
    else:
      print("You are too tired to use your special.")
  def printStats(self):
    super().printStats()
  def defend(self):
    super().defend()
print()
print()
print()
charType = input("Which type of character do you want? Knight has the best defense, Mage has the best attack, and Berserker has the best hp. Mage is the fastest, Knight is in the middle, and Berserker is the slowest. Knight's special is blocking all damage, Mage's skill is increasing attack, and berserker's special is healing some hp.")
if(charType == "Knight"):
  user = Knight()
elif(charType == "Mage"):
  user = Mage()
else:
  user = Berserker()

rand = random.uniform(0,1)
if(rand > 0.66):
  enemy = Knight()
  enemyType = "Knight"
elif(rand > 0.33):
  enemy = Mage()
  enemyType = "Mage"
else:
  enemy = Berserker()
  enemyType = "Berserker"

print("You are up against a " + enemyType + ".")
if(enemy.speed>user.speed):
  print("The enemy is faster than you.")
  winner = 0
  while(winner == 0):
    if(enemy.hp>(enemy.maxHp/2)):
      rand = random.uniform(0,1)
      if(rand > 0.5):
        enemy.attack(user)
      else:
        enemy.special()
    else:
      enemy.defend()
    if(user.hp<=0):
      winner = -1
      break
    command = input("What do you want to do? Attack, Defend, or Special?")
    if(command == "Attack"):
      user.attack(enemy)
    elif(command == "Defend"):
      user.defend()
    else:
      user.special()
    if(enemy.hp<=0):
      winner = 1
      break

else:
  print("You are faster than the enemy.")
  winner = 0
  while(winner == 0):
    command = input("What do you want to do? Attack, Defend, or Special?")
    if(command == "Attack"):
      user.attack(enemy)
    elif(command == "Defend"):
      user.defend()
    else:
      user.special()
    if(enemy.hp<=0):
      winner = 1
      break
    if(enemy.hp>(enemy.maxHp/2)):
      rand = random.uniform(0,1)
      if(rand > 0.5):
        enemy.attack(user)
      else:
        enemy.special()
    else:
      enemy.defend()
    if(user.hp<=0):
      winner = -1
      break
