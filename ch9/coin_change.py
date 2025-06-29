coins = [1, 2, 5]
amount = 11

def change_coin(coins, amount):
    dp = [amount + 1] * (amount + 1) # dp = [amount+1, amount+1, amount+1, ..., amount+1]
    dp[0] = 0 # 要湊出0元的硬幣數亦為0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                print(f"使用 coin = {coin} 時，更新 dp[{i}] = {dp[i]}")
    print(f"dp 狀態（到 i={i}）: {dp}")    
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]
        
print(change_coin(coins, amount))