def power(x, n):
	res = 1
	while n > 0:
		if n & 1: 	# n % 2 != 0:
			res = res * x
		x = x * x
		n = n >> 1 	# int(n / 2)
	return res

ans = power(3, 5)
print(ans)