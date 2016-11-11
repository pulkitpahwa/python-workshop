# Declaration 

## single line 
### Double quotes
a = "apple"
print a

### Single quotes
# b = 'banana'
# print b
# 
## Multi-line declaration
c = """Everyone love Python.
Boys and girls,
Python is easy"""
print c


###    # 1. Immutable: You cant update a string. You can re-assign a new string to old one.
###    
###    # Add 2 strings
###    
###    print a+b
###    print b.__add__(a)
###    
###    # Repeat a string
###    print a*4
###    
###    # Slicing a string: Return characted at a particular index
###    print a[2]
###    
###    ## error in case of out of range.
###    
###    # Range Slicing (Substring)
###    print a[:2]
###    print a[2:]
###    print a[2:4]
###    
###    # Reverse a string
###    print a[::-1]
###    
###    # get the last character of a string
###    print a[-1]
###    
###    # Membership
###    print "banana" in "apple"
###    print "ban" in "banana"
###    print "app" not in "banana"
###    print "apple".__contains__("app")
###    
###    # Length of string
###    
###    print len(a)
###    
###    # Size of string( Size of string in memory (in bytes) )
###    
###    print a.__sizeof__()
###    
###    # Capitalize first letter of a string
###    print a.captialize()
###    
###    # Center align a string. Needs the width of the string. Spaces can be filled with other character too
###    print a.center(70, ".")
###    
###    # Count occurence of string in another string
###    print a.count("a")
###    
###    # check if a string starts with a particular string
###    name = "Rahul Jaiswal"
###    print name.startswith("R")
###    
###    # check if a string end with a particular string
###    name = "Rahul Jaiswal"
###    print name.endswith("Jaiswal")
###    
###    # find the first occurence of a character/ string in another string
###    university = "Amity University Haryana"
###    print university.find("Haryana")
###    print university.find("Noida")
###    
###    and many more
