box = [4,5,3,3,2,2,2,5,6,7]


def first_duplicates(numbers):
    i = 0

    while i < len(numbers):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return numbers[i]

        i += 1

    return None
answer = first_duplicates(box)
print(answer)