def ways_to_sum_memo(n, total):
    memo = {}

    def helper(target):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if target in memo:
            return memo[target]
        
        total_ways = 0
        for i in range(1, n + 1):
            total_ways += helper(target - i)
        
        memo[target] = total_ways
        return total_ways

    return helper(total)


def ways_to_sum_tab(n, total):
    dp = [0] * (total + 1)
    dp[0] = 1

    for i in range(1, total + 1):
        for j in range(1, n + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]

    return dp[total]
