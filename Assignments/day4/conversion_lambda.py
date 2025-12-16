d=int(input("enter distance:"))

m=lambda d:d*1000
cm=lambda m:m*100
mm=lambda cm:cm*10
feet=lambda m:m*3.280
inches=lambda feet:feet*12
c=lambda inches:inches*2.54

def Distance_Converter():
    
    print(f"Killometer to meter={m(d)}")
    
    print(f"meter to centimeter={cm(d)}")
    
    print(f"centimeter to millimeter={mm(d)}")
   
    print(f"meter to feet={feet(d)}")

    print(f"feet to inches={inches(d)}")

    print(f"inches to centimeter={c(d)}")


Distance_Converter()