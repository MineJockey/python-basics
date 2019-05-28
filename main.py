# Notes:
# - Python is a dynamic language so you don't need to
# 	define a variable's type
# - Parentheses are often optional
# - Comments start with # and anything in a comment,
#   won't be run by the computer
# - Counting starts at 0 not 1

# import will load external modules allowing you to use
# the functions within them
# you can use the as statement to create aliases for modules
import learning_files.conditionals as conditionals
import learning_files.functions as functions
import learning_files.loops as loops

if __name__ == '__main__':
    while(True):
        user_input = input('--> ')
        if user_input == 'functions':
            functions.foo()
        elif user_input == 'conditionals':
            pass
        elif user_input == 'loops':
            loops.loops()


# Arithmetic
# +, -, *, /, %, all work with numbers and variables holding numbers
# +=, -=, *=, /=, i.e x += 1 is the same as x = x + 1
x = 1 + 1 # assign 1 + 1 to x
y = 0
y += x  # add x to y

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

# String Array
names = ["Apple", "Orange", "Pear"]

# \n is a newline in a string
print('\n---------------')
print(' For Each Loop')
print('---------------\n')

# For Each Loop
for i in names:
    print(i)

print('\n---------------')
print('   For Loop')
print('---------------\n')

# For Loop
# the range() function can take a min, max, and interval
# value, max is non-inclusive i.e. 101 stops at 100
# example: range(0, 101, 2)
for i in range(5):
    if i == 1:
        print('1, continue')
        # continue will move to the next iteration in the loop
        continue
    elif i == 3:
        print('3, break')
        # the break statement will end the loop
        break
    # if the number doesn't fit the conditions above
    # it will be printed to the console
    print(i)

print('\n---------------')
print('  While Loop')
print('---------------\n')

# Boolean variables hold True or False, 0 or 1
loop = True

# Integer variables hold whole numbers
iterations = 0
max_iterations = 10

# Float variables hold floating point numbers
temp_float = 12.6

print('0 -', max_iterations, '\n')

# The while loop will run as long as the given
# condition or variable is true
# Parentheses are optional
while loop:
    # the += operator adds the given value to
    # the current value of a variable
    iterations += 1
    print(iterations)
    if iterations == max_iterations:
        # break will end a loops execution
        break
