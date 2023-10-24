unit=int(input("Enter total no.of.units:"))
if(unit>0 and unit<=100):
    print("No charges")
elif(unit>100 and unit<=300):
    bal=unit-100
    print("Electricity bill:",bal*10)
elif(unit>300 and unit<=600):
    bal=unit-100
    bal1=bal-300
    print("Electricity bill:",bal*10+bal1*15)
else:
    bal=unit-100
    bal1=bal-300
    bal2=bal1-600
    print("Electricity bill:",bal*10+bal1*15+bal2*20)
