def some_list(numbers: list[int]):
    num = 0
    for num in range(len(numbers)):
        if numbers[num] == 0:
            numbers.remove(numbers[num])
            numbers.append(0)
    return numbers

x = [0,0,2,0]
print(some_list(x))
