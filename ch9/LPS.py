# 最長子“回文”
text = "bbabcbcab"
n = len(text)
dp = [[0]* n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for length in range(2, n+1):
    
    for i in range(n-length+1):
        j = i + length -1
        if text[i] == text[j]:
            dp[i][j] = dp[i+1][j-1]+2
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
print(dp[0][n-1])