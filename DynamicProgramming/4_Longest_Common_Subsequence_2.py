# Longest Common Subsequence (Tabulation)

def lcs(s1, s2):
	m = len(s1); n = len(s2)
	# init db m+1 by n+1
	db = [[0] * (n+1)] * (m+1)

	for i in range(0, m+1):
		db[i][0] = 0
	for j in range(0, n+1):
		db[0][j] = 0

	for i in range(1, m+1):
		for j in range(1, n+1):
			if s1[i-1] == s2[j-1]:
				db[i][j] = 1 + db[i-1][j-1]							
			else:
				db[i][j] = max(db[i-1][j], db[i][j-1])

	return db[m][n]

print(lcs("BAZ", "AXYZ"))	
