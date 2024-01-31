thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple, but str
thistuple = ("apple")
print(type(thistuple))
      
fruits = ("apple", "banana", "cherry")
print(fruits[0])      

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)