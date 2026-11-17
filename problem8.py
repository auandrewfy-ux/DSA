box = [4,5,3,3,2,2,2,5,6,7]

def has_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True

    return False

answer = has_duplicates(box)
print(answer)