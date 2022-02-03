zaehlen_bis = int(input("Zählen bis (maximal 5): "))
zahl = 0
limit = 5
while zahl < zaehlen_bis:
    print(zahl)
    if zahl == limit:
        print("Beim Limit", limit, "ist Schluss")
        break
    zahl = zahl+1
else:
    print("Limit wurde nicht erreicht")
