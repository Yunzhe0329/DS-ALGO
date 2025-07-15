# input example
weight = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

def knapback(weight, value, capacity):
    n = len(weight)
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(n+1):
        for w in range(1, capacity+1):
            if weight[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight[i-1]]+values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[i][w]

print(knapback(weight, values, capacity))
    
    