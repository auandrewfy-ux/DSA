box = [4,5,3,3,2,2,2,5,6,7]
target = 7


def find_largest(numbers):
    largest = 0
    for i in numbers:
        if i > largest:
            largest = i
    print(largest)
find_largest(box)

def find_smallest(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    print(smallest)
find_smallest(box)

def list_sum(numbers):
    total = numbers[0]
    for i in numbers:
        total += i
    print(total)


list_sum(box)

def count_even(numbers):
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total += 1
    print(total)
count_even(box)

def count_occurrences(numbers, target):
    total_occ = 0
    for i in numbers:
        if target == i:
            total_occ += 1
    print(total_occ)

count_occurrences(box, target)

def find_number(numbers, target):
    finder = numbers[i]
    for i in range(len(numbers)):
        if target == numbers:
            print(finder)

find_number(box, target)


