box = [6,7,54,4,5,6]

def list_sum(numbers):
    total = 1
    for i in numbers:
        total = total + i
    if not numbers:
        return 0
    print(total)
list_sum(box)
