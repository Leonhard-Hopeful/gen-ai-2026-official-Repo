def add(a, b):
    return a + b;


add(2, 3)

# SOLUTION : args
# *-> collect all extra postional arguments into one turple
def add_dynamic(*args):
    print(args)


add_dynamic(1,3,4,5,6,7)

# add any number of items

def any_items(*args):
    total=0;
    
    for number in args:
        total+=number;
    return total


# Introduciing people
# *args  is just a convention we can use anyhting eg *people

def introduce_people(*args):
    for person in args:
        print("Hello", person)
introduce_people("John", "Mary", "Peter")
