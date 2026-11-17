box = [5,6,2,4,2,3,4,44,66,772]

def count_even(numbers):
    even_num = 0
    for i in numbers:
        if i % 2 == 0:
            even_num = even_num + 1
    print(even_num)
count_even(box)