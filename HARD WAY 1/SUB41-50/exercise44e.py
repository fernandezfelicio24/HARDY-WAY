"""
Inheritance is useful,but another way to do the exact same thing is just to use other classes and modules, rather than relyon implicit inheritance.
If you look at the three ways to exploit inheritance,two of the three involve writing new code to replace or alter functionality.   
"""
#COMPOSITION

class Other(object):
    
    def override(self):
        print("OTHER override")
        
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered")
        
class Child(object):
    
    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE OTHER altered()") 
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")       

son = Child()

son.implicit()
son.override()
son.altered()