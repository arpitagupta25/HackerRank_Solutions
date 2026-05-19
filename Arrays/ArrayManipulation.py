def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for a, b, k in queries:
        arr[a - 1] += k
        
        if b < n:
            arr[b] -= k

    max_value = 0
    current = 0

    for value in arr:
        current += value
        max_value = max(max_value, current)

    return max_value
