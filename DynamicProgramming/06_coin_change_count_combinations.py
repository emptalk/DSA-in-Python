#coins = [2, 5, 3, 6]
#sum = 10

def getCount(coins, n, sum):
	if sum == 0:
		return 1
	if n == 0:
		return 0

	# not include any last coin
	res = getCount(coins, n-1, sum)
	if coins[n-1] <= sum: 
		# includes at least one last coin
		res += getCount(coins, n, sum - coins[n-1])

	return res

print(getCount([2, 5, 3, 6], 4, 10))

def getCount2(coins, n, sum):
	# dp[sum][coin type count]
	dp = [[0 for _ in range(n+1)] for _ in range(sum+1)]

	for i in range(0, n+1):
		dp[0][i] = 1 # if sum is 0, count is always 1
	
	for i in range(1, sum+1):
		dp[i][0] = 0 # if there are no coins and sum > 0, count is always 0

	for i in range(1, sum+1):
		for j in range(1, n+1):
			dp[i][j] = dp[i][j-1] # exclude j th coin type
			if coins[j-1] <= i: # coins[j-1]: j th coin
				dp[i][j] += dp[i - coins[j-1]][j]

	for i in range(0, sum+1):
		for j in range(0, n+1):
			print(dp[i][j], end=' ')
		print()


	return dp[sum][n]

print(getCount2([2, 5, 3, 6], 4, 10))
