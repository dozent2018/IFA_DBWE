"""var_demo.py demonstriert die Auswertung einer Auflistung
beliebig vieler Parameter. Eine Reihe von Zahlen wird mit dem
Wert der letzten angeggebenen Zahl multipliziert"""
def mult_with_last( *numbers) -> None:
    last = numbers[-1]
    for num in numbers[0:-1] :
        print(num * last)

mult_with_last(3, 9, 7, 10)

