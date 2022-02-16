"""reihenfolge.py demonstriert die Auswirkung der Reihenfolge 
von verschiedenen Parameterarten in der Funktions-Definition"""

def p_order1( par1, par2, *args):
    print('In p_order1 arg1:', par1, ' arg2:', par2, ' *args:', args)

def p_order2( *args, par1='foo', par2='bar'):
    print('In p_order2 arg1:', par1, ' arg2:', par2, ' *args:', args)

def p_order3( par1, par2, *args, **kwargs):
    print('In p_order3 arg1:', par1, ' arg2:', par2, ' *args:', args, '**kwargs:', kwargs)

def p_order4( par1, par2, *args, par4, par5):
    print('In p_order4 arg1:', par1, ' arg2:', par2, ' *args:', args, 'arg4:', par4, 'arg5:', par5)
    


p_order1(1, 2, 3, 4)
p_order2(1, 2, 3, 4)
p_order3(1, 2, 3, 4, a=5, b=6)
p_order4(1, 2, 3, 4, par4=5, par5=6)

