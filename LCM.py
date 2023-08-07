a = int(input("Enter a : "))
b = int(input("Enter b : "))
st = max(a,b)
lcm = 0
while lcm == 0 and st <= a*b :
    d1 = st % a
    d2 = st % b
    if d1 == 0 and d2 == 0 :
        lcm = st
    st += 1
if lcm != 0 :
    print(lcm)
else :
    print(a*b) 