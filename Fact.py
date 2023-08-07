num=int(input("Enter your number :"))
i = 0.0
m=1.0
k=1
while i == 0.0 :
    i = num % k
    if i == 0.0 :
        m = k*m
    k=k+1
if m == num :
    print("yes")
elif m != num :
    print("no")