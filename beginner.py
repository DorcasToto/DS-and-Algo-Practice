mylist = ["apple", "banana", "cherry","test"]
print(mylist[2:])
print(mylist[:2])
print(mylist[1:2])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist.insert(2, "watermelon")
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
thislist.pop(1)
print(thislist)
# for x in thislist:
#   print(x)
# for i in range(len(thislist)):
#   print(thislist[i])
[print(x) for x in thislist]

thislist2 = [100, 50, 65, 82, 23]
thislist2.reverse()
# thislist2.sort()
# thislist2.sort(reverse = True)
print(thislist2)

# mylist = thislist.copy()
# print(mylist)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

(green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
print(mytuple)

thisset = {"apple", "banana", "cherry"}
print(thisset)
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


