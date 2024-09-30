info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")
  
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info) 


info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)


info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)