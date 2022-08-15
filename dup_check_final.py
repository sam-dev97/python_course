#  Retornar o primeiro número duplicado de uma lista, caso contrário retornar -1

def duplicate_finder(lista):
    nums = set()
    first_dup = -1
    for num in lista:
        if num in nums:
            first_dup = num
            break

        nums.add(num)

    return first_dup


print(duplicate_finder([1, 2, 3, 3, 2, 1]))
