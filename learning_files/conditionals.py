# Conditional Operators:
# == checks if two values are equal and returns true or false
# != checks if two values are not equal and returns true or false
# >, <, >=, <=, greater than, less than operators

# if statements with execute a block of code if the given condition
# returns true
if 1 == 1:
    equal = True
    print("1 does equal 1 after all")
# elif statements will be tested one after another if the previous
# if or elif wasn't true
elif 1 != 1:
    # this will never be reached
    # the pass statement does nothing, it's a blank function of sorts
    pass
# if all other connected if/elif statements fail this will be run
else:
    # this will also never be reached
    pass
