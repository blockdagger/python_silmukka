import random

counter = 1 

print ("Tervetuloa numeronarvauspeliin")

tietokoneen_luku = random.randint(0,10)

print ("Osaatko arvata luvun jonka valitsin väliltä 0-10")

arvaus = input("Arvaa numero \n")
arvaus = int(arvaus)

while True: 
  if arvaus == tietokoneen_luku:
    print ("arvasit" + str(counter)+ "kertaa")
    break
  elif arvaus != tietokoneen_luku:
    arvaus = input("Arvaa numero uudestaan \n")
    arvaus = int(arvaus)
    counter = counter+1
  