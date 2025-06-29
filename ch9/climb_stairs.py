# n => stairs, 一次只能爬一階或兩階
def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1 #不動
    dp[1] = 1 #爬一階

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    return dp[n]

n = 5
print(f'總共有{climb_stairs(n)}種爬法')

