box = [3,4,3,23,45,3,4,5,6,8,3,4,34,56,10,87,98,91,11,17]
target = 10


def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num

        elif num != largest and (second is None or num > second):
            second = num

    print(second)


second_largest(box)