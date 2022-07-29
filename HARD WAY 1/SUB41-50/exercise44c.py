"""
The third way to use inheritance is a special case of overriding where you want to alter the behavior
before or after the Parent class’s version runs. You ﬁrst override the function
just like in the last example, but then you use a Python built-in function named
super to get the Parent version to call
"""

class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered() ")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()