#NAMES, VARIABLES, CODE, FUNCTIONS


#THIS ONE IS LIKE YOUR SCRIPTS WITH ARGV

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
    
#OK, THAT *ARGS IS ACTUALLY POINTLESS, WE CAN JUST DO THIS

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#THIS JUST TAKES NO ARGUMENT
def print_one(arg1):
    print(f"arg1: {arg1}")
    
def print_none():
    print("I got nothin")
    

print_two("Felicio", "Fernandes")
print_two_again("Philps", "Patric")
print_one("First !")
print_none()