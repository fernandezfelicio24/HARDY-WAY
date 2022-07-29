class Parent(object):
    
    def override(self):
        print("PARENT override()")
    
    def implicit(self):
        print("PARENT implicit()")
        
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT ALTERED()")
        
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.implicit()

dad.altered()
son.altered()