"""
The use of pass under the class Child: is how you tell Python that you want an empty block.
This creates a class named Child but says that there’s nothing new to deﬁne in it. 
Instead it will inherit all of its behavior from Parent.
"""
class Parent():
    
    def implicit(self):
        print("PARENT implicit()")
        
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()