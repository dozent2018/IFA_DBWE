gedicht_liste = ['Der Panther (von Robert Gernhard)\n', 
                 'Der Panther, der Panther\n', 
                 'Erst lag er, dann stand er\n', 
                'worauf er so erschrak,\n', 'dass er gleich wieder lag']

with open('out.txt', 'w') as out_file:
    out_file.writelines(gedicht_liste)