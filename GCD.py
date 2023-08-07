a =int(input("enter a : "))
b = int(input("enter b : "))
if a > b :
    max = a
    min = b
else :
    max = b
    min = a
m = max - min
gcd = 0
if m == 0 :
    gcd = 1

while gcd == 0 :
    d1 = max % m
    d2 = min % m
    if d1 == 0 and d2 == 0 :
        gcd = m
    m -= 1 
print(gcd)