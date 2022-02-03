# import_demo1.py zeigt den Import einer eigenen Funktion
from myfunctions import is_int

mystring = '1001'
myint = 0

if is_int(mystring) == True :
    myint = int(mystring)
    print(myint)
else :
    print("Keine Zahl")
    