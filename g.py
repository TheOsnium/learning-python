# APPEND ITEMS(To add an item to the end of the list)
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
mylist.append('orange')
print(mylist)

#INSERT ITEMS(To insert a list item at a specified index)
mylist.insert(3, 'apple')
print(mylist)

#EXTEND LIST(To append elements from another list to the current list)
thislist = ["apple", "banana", "cherry"]
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
mylist.extend(thislist)
print(mylist)

# REMOVE AN ITEM FROM LIST
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index(The pop() method removes the specified index)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.


#The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

del thislist

# CLEAR THE LIST
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# LOOPING THROUGH THE LIST(Print all items in the list, one by one:)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
[print(x) for x in thislist]
for i in range(len(thislist)):
  print(thislist[i])

#List Comprehension
fruits = ['apple' 'banana', 'mango', 'apricot']
newlist = [x for x in fruits if 'a' in x]
print(newlist)

#CONDITION
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple"
newlist = [x for x in fruits if x != 'apple']
print(newlist)
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]

print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# copy of a list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# TUPLE
mytuple = ('a', 'b', 'c', 'd')
print(len(mytuple))

thistuple = ("apple",)  #One item tuple, remember the comma
print(type(thistuple))
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)

# trying some basic things on tuple
print(thistuple[2])
print(thistuple[-2])  #-2 refers to the second last item 
print(thistuple[1:2]) # here 2 is not included
print(thistuple[:4]) #This example returns the items from the beginning to, but NOT included, "kiwi"
print(thistuple[2:])
print(thistuple[-4:-1]) #This example returns the items from index -4 (included) to index -1 (excluded)
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

y = ('orange',)
thistuple += y
print(thistuple)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#Python - Unpack Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#USING ASTERISK *

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# join a tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

thislist = {'a', 'b'}
print(type(thislist))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

for x in thisset:
  print(x)
print('banana' in thisset)

thisset.add('orange')
print(thisset)

tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset.remove("banana")

print(thisset)

#Remove the last item by using the pop() method
x = thisset.pop()

print(x)

print(thisset)

#The clear() method empties the set
thisset.clear()

print(thisset)

#The del keyword will delete the set completely
del thisset

# looping in a set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Keep the items that exist in both set x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
z = x.intersection(y)  # easy one

print(z)

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


# DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

#You can access the items of a dictionary by referring to its key name, inside square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["year"]
print(x)

x = thisdict.keys()  #The keys() method will return a list of all the keys in the dictionary
print(x)

# TO ADD SOMETHING IN DICTIONARIES
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)
car["color"] = "white"  # IMPORTANT
print(x)

car = {
  'brand': 'suzuki',
  'model': 'baleno',
  'year': '2021',
}
x = car.values()
print(x)
car['year'] = 2019
print(x)

#Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

del thisdict['brand']
print(thisdict)

thisdict.clear()  #The clear() method empties the dictionary
print(thisdict)

# LOOPING 
mydict = {
  'name': 'ayush sharma',
  'class': 'B tech',
  'house': 'meerut',
  }

for x in mydict:
  print(x)

  print(mydict[x]) #Print all values in the dictionary, one by one

for x in mydict.keys(): #You can use the keys() method to return the keys of a dictionary
  print(x) 

for x, y in mydict.items(): #Loop through both keys and values, by using the items() method
  print(x, y)

# COPY A DICTIONARY

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# if you want to add three dictionaries into a new dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

#Python If ... Else
a = 500
b = 510
if b > a:
  print('hurray')

# Elif
a = 58
b = 58
if a > b:
  print('oh')
elif a == b:
  print('savage')

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200

if b > a:
  pass  #if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

#The while Loop
i = 1
while i < 6:
  print(i)
  i = i+1

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

import datetime

x = datetime.datetime.now()
print(x)