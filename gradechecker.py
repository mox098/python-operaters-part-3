print("enter marks for 5 subjects")

mark1=int(input("enter a mark"))
mark2=int(input("enter a mark"))
mark3=int(input("enter a mark"))
mark4=int(input("enter a mark"))
mark5=int(input("enter a mark"))

total=mark1+mark2+mark3+mark4+mark5
average=total/5

if average>=91 and average<=100:
    print("average is A1")
elif average>=81 and average<91:
    print("average is A2")
elif average>=71 and average<81:
    print("average is B1")
elif average>=61 and average<71:
    print("average is B2")
elif average>=51 and average<61:
    print("average is C1")
elif average>=41 and average<51:
    print("average is C2")
elif average>=31 and average<41:
    print("average is D")
elif average>=21 and average<31:
    print("average is E1")
elif average>=11 and average<21:
    print("average is E2")

else:
    print("Invalid input!")

