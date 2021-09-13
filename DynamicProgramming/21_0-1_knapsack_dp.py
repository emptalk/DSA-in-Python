# time: theta(nW)
# aux space: theta(nW)
def knapsack(W, wt, val, n):
	dp = [[None for _ in range(W+1)] for _ in range(n+1)]
	for i in range(W+1):
		dp[0][i] = 0
	for i in range(n+1):
		dp[i][0] = 0
	for i in range(1, n+1): # wt[0] ~ wt[n]
		for j in range(1, W+1):
			if wt[i-1] > j:
				dp[i][j] = dp[i-1][j] # can not put wt[i-1] which matches i for dp
			else:
				dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],
							   dp[i-1][j])

	return dp[n][W]

ans = knapsack(10, [5,4,6,3],[10,40,30,50],4)
print(ans)