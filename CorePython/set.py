s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
  print(value)
 
s1 = {2, 4, 2, 6}
s2 = {1,3,5}
print(s1.union(s2))
s1.update(s2)
print("after update value of s1 =",s1)

s1 = {2, 4, 2, 6}
s2 = {1,3,5,2,6}
s3 = s1.intersection(s2)
print(s3)
s1.intersection_update(s2)
print(s1)


s1 = {2, 4, 2, 6}
s2 = {1,3,5,2,6}
s3 = s1.difference(s2)
print(s3)
s1.difference_update(s2)
print(s1)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
    
    
    