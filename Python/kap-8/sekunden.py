from datetime import datetime
from time import sleep
from random import randint
anzahl = 0 
while anzahl < 10:
    sekunde = datetime.today().second
    if sekunde % 2 == 0:
        print(sekunde, "ist eine gerade Sekunde")
    else:
        print(sekunde, "ist eine ungerade Sekunde")  
    wartezeit = randint(1,3)
    sleep(wartezeit)
    anzahl += 1