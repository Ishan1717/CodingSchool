#Gather the user's name, birthday, and favorite color
#Print the user's name, AGE, and favorite color back
##Assume age range between 0 and 100 (exclusive)

##Additionally:
#Ask for user's month and day of birth;
#Additionally print out the user's Zodiac sign

'''
#Aries: 21 March - 20 April
#Taurus: 21 April - 21 May
#Gemini: 22 May - 21 June
#Cancer: 22 June - 22 July
#Leo: 23 July - 22 August
#Virgo: 23 August - 23 September
#Libra: 24 September - 23 October
#Scorpio: 24 October - 22 November
#Sagittarius: 23 November - 21 December
#Capricorn: 22 December - 20 January
Aquarius: 21 January - 19 February
Pisces: 20 February - 21 March
'''

##Assume user will enter days, months, and years as integer numbers


name = input("What is your name?")
year = input("What year were you born?")
month = input("What month were you born in?")
day = input("What day were you born on?")
color = input("What is your favorite color?")
print("Name: " + name)
print("Age: " + str(2019-int(year)))
print("Favorite color: " + color)
if(((month==3) and (day>20)) or ((month==4) and (day<21))):
  print("Zodiac Sign: Aries")
elif(((month==4) and (day>20)) or ((month==5) and (day<22))):
  print("Zodiac Sign: Taurus")
elif(((month==5) and (day>21)) or ((int(month)==6) and (int(day)<22))):
  print("Zodiac Sign: Gemini")
elif(((month==6) and (day>21)) or ((month==7) and (day<23))):
  print("Zodiac Sign: Cancer")
elif(((month==7) and (day>22)) or ((month==8) and (day<23))):
  print("Zodiac Sign: Leo")
elif(((month==8) and (day>22)) or ((month==9) and (day<24))):
  print("Zodiac Sign: Virgo")
elif(((month==9) and (day>23)) or ((month==10) and (day<24))):
  print("Zodiac Sign: Libra")
elif(((month==10) and (day>23)) or ((month==11) and (day<23))):
  print("Zodiac Sign: Scorpio")
elif(((month==11) and (day>22)) or ((month==12) and (day<22))):
  print("Zodiac Sign: Sagittarius")
elif(((month==12) and (day>21)) or ((month==1) and (day<21))):
  print("Zodiac Sign: Capricorn")
elif(((month==1) and (day>20)) or ((month==2) and (day<20))):
  print("Zodiac Sign: Aquarius")
else:
  print("Zodiac Sign: Pisces")
