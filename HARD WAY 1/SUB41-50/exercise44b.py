"""
The problem with having functions called implicitly is sometimesyouwantthechildtobehavedifferently.
In this case you want to override the function in the child,effectively replacing the functionality.
Todo this just deﬁne a function with the same name in Child. 
"""

class Parent(object):
    
    def override(self):
        print("PARENT override()")
        
class Child(Parent):
    
    def override(self):
        print("CHILD override()")
        

dad = Parent()
son = Child()

dad.override()
son.override()