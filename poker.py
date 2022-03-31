import math
# 斗地主中非地主至少模到一个普通炸的概率计算
# 计算它的反面，没有摸到一个炸的概率，13个数字每个摸到的个数都在0~3之间，它们的张数总共有15或16或17张
# 定义dp[i][j]为前i个数字中抽到j张的组合数
def boom():
    dp = [[0]*18 for _ in range(14)]
    dp[0][0] = 1
    for i in range(1, 14):
        dp[i][0] = 1
        for j in range(1, 18):
            dp[i][j] = dp[i-1][j]
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]*4
            if j-2 >= 0:
                dp[i][j] += dp[i-1][j-2]*6
            if j-3 >= 0:
                dp[i][j] += dp[i-1][j-3]*4
    # 斗地主摸到普通炸的概率
    # dp[13][15] + 2*dp[13][16] + dp[13][17]
    return dp[13][13]
# 四人牌摸到炸的概率
print(1-boom()/math.comb(52, 13))