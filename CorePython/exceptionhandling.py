a = int(input("enter the number = "))
print("multipcation table of a ")
try:
    for i in range(1 , 11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except :
    print("invalid input")
    print("valid input")
print("you want to try again")


# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")