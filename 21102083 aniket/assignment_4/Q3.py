import random
a=random.randint(1,10)
b=random.randint(1,10)
c=int(input(f"{a} X {b} = "))
if(c==a*b):
    print("right")
else:
    print(f"wronge,right answer is {a*b}")