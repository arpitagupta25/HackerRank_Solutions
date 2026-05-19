def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    answers = []

    for i in range(len(queries)):
        q = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]

        idx = (x ^ lastAnswer) % n

        if q == 1:
            arr[idx].append(y)

        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers
    
