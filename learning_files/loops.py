def loops():
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


if __name__ == '__main__':
    loops()
