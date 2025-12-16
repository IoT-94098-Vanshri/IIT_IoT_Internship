d = int(input("Enter Distance:"))

def distance_converter(d):
    m = d*1000 
    print("kilometer to meter:",m)
    cm = m*100
    print("meter to centimeter:",cm)
    mm = cm*10
    print("centimeter to milimeter:",mm)
    feet = m*3.280
    print("meter to feet:",feet)
    inches = feet*12
    print("feet to inches:",inches)
    c = inches*2.54
    print("inches to centimeter:",c)

def print_result():
   distance_converter(d)
    
print_result()