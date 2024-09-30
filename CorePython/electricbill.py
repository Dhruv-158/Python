Amount = int(input("Enter an amount = "))
Unit = int(input("Enter an unit = "))
if Unit <= 100:
    print("Total value is = ",Amount)
elif Unit>=100 and Unit<=200:
    print("Total value is = ",((Unit - 100)*5)+Amount)
elif Unit>=200 and Unit>=300:
    if Unit>=200:
        a = (Unit - 100) * 5
        b = (Unit - 200) * 10
        print("Total Amonut is = ",a+b+Amount)