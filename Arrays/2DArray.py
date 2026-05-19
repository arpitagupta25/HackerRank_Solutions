def hourglassSum(arr):
    max_sum = float('-inf')

    for i in range(4):        # rows 0 to 3
        for j in range(4):    # columns 0 to 3
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1]
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            max_sum = max(max_sum, current_sum)

    return max_sum
