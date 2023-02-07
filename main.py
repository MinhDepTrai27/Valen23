import random, os, time
name = input("Name: ")
print(f"Ủa {name} à=))")
for t in range(5, -1, -1):
    print(f'Chờ tớ xíu, tớ mang cái này tặng cậu nè, chờ tớ {t} giây nha:33', end='\r')
    time.sleep(1)
blank = "".join([' ' for x in range(int(round((21-len(name))/2)))])
name = blank+name+blank
logo = f"""   ************     ************
  ****      ***** *****      ****
 ***           *****           ***
 **              *              **
 **                             **
  ***                         ***
   ****{name}****
     ****                  ****
       ****             ****
         ****         ****
           ****     ****
             ***   ***
              *** ***
               *****
                 *


I love you chut chut:333
"""
colors = [x for x in range(91, 98)]
while True:
    print("".join([f"\033[{random.choice(colors)}m{x}" for x in logo]))
    time.sleep(1/10)
    os.system('cls' if os.name == 'nt' else 'clear')
