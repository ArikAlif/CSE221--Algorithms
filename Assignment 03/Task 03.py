a, b = map(int, input().split())
m = 107
def fast_mod(a, b, m):
    if b == 0:
        return 1
    calc = fast_mod(a, b//2, m)
    calc = (calc * calc) % m
    if b % 2 == 1:
        calc = (calc * a) % m
    return calc
    
print(fast_mod(a, b, m))