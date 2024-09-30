marks = [12, 56, 32, 98, 12,  45, 1, 4]

# x = 0
# for mark in marks:
#   print(mark)
#   if(x == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):
  print(f"{mark} index = {index}")
  print("Harry, awesome!") if index == 3 else None
    