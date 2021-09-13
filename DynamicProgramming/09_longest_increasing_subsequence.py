# time: theta(n^2)
# aux space: theta(n)
def lis(arr, n):
	dp = [None for _ in range(n)]
	dp[0] = 1

	for i in range(1, n):
		dp[i] = 1
		for j in range(i):
			if arr[j] < arr[i]:
				dp[i] = max(dp[i], dp[j]+1)
	
	return max(dp)	

print(lis([3,4,2,8,10,5,1], 7))				
