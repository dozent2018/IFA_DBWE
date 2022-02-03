"""reihenfolge.py demonstriert die Auswirkung der Reihenfolge 
von verschiedenen Parameterarten in der Funktions-Definition"""

def p_order1( par1, par2, *args):
    print('In p_order1 arg1:', par1, ' arg2:', par2, ' *args:', args)

def p_order2( *args, par1='foo', par2='bar'):
    print('In p_order2 arg1:', par1, ' arg2:', par2, ' *args:', args)

def p_order3( *args, par1, par2):
    print('In p_order3 arg1:', par1, ' arg2:', par2, ' *args:', args)

p_order1(1, 2, 3, 4)
p_order2(1, 2, 3, 4)
p_order3(1, 2, 3, 4)

