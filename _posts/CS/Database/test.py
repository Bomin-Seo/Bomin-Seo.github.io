def solution(temperature, t1, t2, a, b, onboard):
    t1 += 10
    t2 += 10
    temperature += 10

    dp = [[1e7] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0

    for i in range(1, len(onboard)):
        isonboard = onboard[i]

        for j in range(51):
            
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + (a if j != temperature else 0))
            if j < 50:
                dp[i][j] = min(dp[i][j], dp[i-1][j+1] + (a if j != temperature else 0))
            dp[i][j] = min(dp[i][j], dp[i-1][j] + (b if j == temperature else 0))

        if isonboard:
            for j in range(51):
                if j < t1 or j > t2:
                    dp[i][j] = 1e7
    print(dp)

    return min(dp[-1])

print(solution(28,18,26,10,8,[0, 0, 1, 1, 1, 1, 1]))