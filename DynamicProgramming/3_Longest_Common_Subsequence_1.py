def lcs(s1, s2, m, n):
	if m == 0 or n == 0:
		return 0

	if s1[m-1] == s2[n-1]:
		return 1 + lcs(s1, s2, m-1, n-1)
	else:
		return max( lcs(s1, s2, m-1, n), \
					lcs(s1, s2, m, n-1) )

#print(lcs("AXYZ", "BAZ", 4, 3))

# memoization
memo = None
def lcs_run(s1, s2, m, n):
	global memo
	# initialize (m+1) x (n+1) multidimentional array
	memo = [[-1 for c in range(n+1)] for r in range(m+1)]
	return lcs2(s1, s2, m, n)	

def lcs2(s1, s2, m, n):
	global memo

	if memo[m][n] != -1:
		return memo[m][n]
	
	if m == 0 or n == 0:
		memo[m][n] = 0
	else:
		if s1[m-1] == s2[n-1]:
			memo[m][n] = 1 + lcs2(s1, s2, m-1, n-1)
		else:
			memo[m][n] = max(lcs2(s1, s2, m-1, n), \
							 lcs2(s1, s2, m, n-1))

	return memo[m][n]

print(lcs_run("AXYZ", "BAZ", 4, 3))