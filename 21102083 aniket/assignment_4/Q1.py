grades=int(input("enter your grades"))
g=grades
if(g<0 or g>100):
    print("invalid")
elif(g<25):
    print("f")
elif(g<45):
    print("e")
elif(g<50):
    print("d")
elif(g<60):
    print("c")
elif(g<80):
    print("b")
elif(g<100):
    print("a")
