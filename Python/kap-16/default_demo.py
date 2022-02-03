"default_demo.py demonstriert Default-Werte für Parameter"
def hallo(begruessung: str = 'Hallo', name: str = '?' ) -> None :
    print(begruessung, name)

hallo('Moin', 'Karin')
hallo(name='Karin')
hallo(begruessung='Hi')
hallo()

