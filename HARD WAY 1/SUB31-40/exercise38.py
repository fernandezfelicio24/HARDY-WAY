# DOING THINGS TO LISTS

# pop is inbuilt function that removes and return the last value from the List
#Or The given index value.

ten_things = "Apples Oranges Crows Telephone Light Sugar"


print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]
"""
panjan = len(stuff)
print(panjan)
print("============")
"""

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now. ")

print("======================")
print("There we go: ", stuff)


print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) #what ? cool!
print('#'.join(stuff[3:5])) #super stellar
