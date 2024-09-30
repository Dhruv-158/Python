# f = open('note2','a')
# f.write('\n my nam is ')
# f.close()
 
# with open('note','r') as f:
#     print(f.read())

# readline() :- read line by line

# The code line.split(",")
# "apple,banana,orange". When you apply split(",") to this sentence, you get a list like this: ["apple", "banana", "orange"].
# i = 0
# f = open('note2', 'r')
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks opf student {i} in Maths is {m1}")
#     print(f"marks opf student {i} in Science is {m1}")
#     print(f"marks opf student {i} in English is {m1} \n\n")
#     print(type(m1))
#     m1 = int(m1)
#     print(type(m1))

# f = open('note2', 'w')
# lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
# f.writelines(lines)
# f.close() 



# function seek() and tell()

# with open('note','r') as f:
#     print(type(f))
    
#     f.seek(10) 
    
    # help of seek(10) first we ignore the 10 character of the line and count afyter 10 character
    # print(f.tell())
    # data = f.read(5)
    # print(data)


# with open('note', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)

#   # Save the current position
#   current_position = f.tell()

#   # Seek to the saved position
#   f.seek(current_position)


# truncate() 

# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)
  
# #   truncate(5)means in this new file you store only five charavcter in this file  

# with open('sample.txt', 'r') as f:
#   print(f.read())
