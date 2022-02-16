def ggt_i(x: int, y: int) -> int :
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x

def ggt_r(x: int, y: int) -> int :
    if x == 0: return y
    if y == 0: return x
    return ggt_r( y, x % y )

if __name__ == '__main__':
    import time, sys
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print( ggt_i(x, y) )
    print( ggt_r(x, y) )