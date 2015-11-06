def fib_iterative(num):
    if num < 0:
        print('invalid input')
        return -1
    if num == 0 or num == 1:
        return num

    index = 2
    last = 1
    second_last = 0

    while index < num + 1:
        temp = last
        last += second_last
        second_last = temp
        index += 1

    return last

def print_fib(num):
    if num < 0:
        print('invalid input')
        return
    if num == 0 or num == 1:
        print(num, end=' ')

    index = 2
    last = 1
    second_last = 0

    print(0, 1, end=' ')
    while index < num + 1:
        temp = last
        last += second_last
        second_last = temp
        print(last, end=' ')
        index += 1

    print('')

def fib_recursive(num):
    if num < 0:
        print('invalid input')
        return -1
    if num == 0 or num == 1:
        return num

    return fib_recursive(num - 1) + fib_recursive(num - 2)

def fib_with_memoisation(num, calculated_fib=dict()):
    if num < 0:
        print('invalid input')
        return -1
    if num == 0 or num == 1:
        return num

    if num in calculated_fib:
        return calculated_fib[num]

    calculated_fib[num] = fib_with_memoisation(num - 1, calculated_fib) + \
           fib_with_memoisation(num - 2, calculated_fib)
    return calculated_fib[num]


#print(fib_with_memoisation(int(input())))
#print(fib_iterative(int(input())))
#print_fib(int(input()))
