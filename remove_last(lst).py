def remove_last(lst):
    lst.pop()


numbers = [10, 20, 30, 40]

print("Before function call:", numbers)

remove_last(numbers)

print("After function call:", numbers)