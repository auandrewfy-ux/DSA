box = [12, 45, 80, 23, 100, 5]

def find_largest(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
        largest = i
    print(largest)

find_largest(box)
