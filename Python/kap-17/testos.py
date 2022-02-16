import os
home = os.getcwd()
print('Aktuelles verzeichnis:', home)
print( 'Einträge: ', os.listdir(home) )
os.mkdir('Unterverzeichnis')
os.chdir('Unterverzeichnis')
print('Aktuelles verzeichnis:', os.getcwd())
print( 'Einträge: ', os.listdir() )
os.chdir(home)
os.rmdir('Unterverzeichnis')
os.r