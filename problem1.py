box = [12, 45, 80, 23, 100, 5]

def find_largest(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    print(smallest)

find_largest(box)