def five(numbers, threshold):
    return list(filter(lambda x: x > threshold, numbers))

num = [1, 5, 10, 3, 8]
threshold = 5

result = five(num, threshold)
print("List of numbers greater than threshold", result)
