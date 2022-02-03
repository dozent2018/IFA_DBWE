# import_demo2.py zeigt den Import einer eigenen Funktion
import myfunctions

mystring = '1001'
myint = 0

if myfunctions.is_int(mystring) == True :
    myint = int(mystring)
    print(myint)
else :
    print("Keine Zahl")
