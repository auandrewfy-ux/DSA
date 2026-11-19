numbers = [10, 20, 30, 20, 20]
target = 20

def count_occurrences(numbers, target):
    count = 0

    for number in numbers:
        if number == target:
            count += 1

    print(count)
count_occurrences(numbers, target)