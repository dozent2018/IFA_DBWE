"""var_kwargs_demo zeigt, was die Angabe von '**' bei einem
Parameternamen bewirkt"""
def any_kwargs( **kwargs) -> None :
    print(len(kwargs), 'Argumente übergeben')
    for arg in kwargs.keys() :
        print('name:', arg, 'wert:', kwargs[arg])

any_kwargs(arg1=10, arg2=11, arg3=12, arg4='letztes')

