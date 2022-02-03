a = 1
b = 1
stellen = int( input( "Wieviele Fibonacci-Zahlen ausgeben? "))
for zahl in range(8):
    print(a)
    a, b = b, a + b
    # Python unterstützt Mehrfach-Zuweisungen. Ohne sie müsste 
    # man eine zusätzliche Variable zum Zwischenspeichern des Ergebnisses 
    # von a + b verwenden und das Programm wäre um ein paar Zeilen länger
      