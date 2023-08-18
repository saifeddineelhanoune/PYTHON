def isValidCombination(combination):
    for i in range(len(combination) - 1):
        if combination[i] >= combination[i + 1]:
            return False
    return True


def hasDuplicate(combination, index):
    for i in range(index):
        if combination[i] == combination[index]:
            return True
    return False


def displayCombination(combination):
    combination_str = ', '.join(map(str, combination))
    print(combination_str, end=" ")


def generateCombinations(combination, index, n, current_digit):
    if index == n:
        if isValidCombination(combination):
            displayCombination(combination)
        return

    for digit in range(current_digit, 10):
        combination[index] = digit
        if not hasDuplicate(combination, index):
            generateCombinations(combination, index + 1, n, digit + 1)


def print_combn(n):
    if n <= 0 or n >= 10:
        print("Invalid input. n should be between 1 and 9.")
        return

    combination = [0] * n
    generateCombinations(combination, 0, n, 0)


n = int(input("Enter the value of n: "))
print_combn(n)
