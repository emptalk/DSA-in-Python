# fibonacci number

def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-1) + fib(n-2)

print(fib(5))

# use memoization
memo = None

def fibrun(n):
	global memo
	# fill memo with not possible answer, in this case -1
	memo = [-1] * (n + 1) # memo[9] ~ memo[n]
	return fibm(n)

def fibm(n):
	# if fibm(n) is not memoized, calculate	fibm(n)
	# otherwise just reuse memo[n]
	global memo

	if memo[n] == -1:
		if n == 0 or n == 1:
			res = n
		else:
			res = fibm(n-1) + fibm(n-2)

		memo[n] = res

	return memo[n]


print(fibrun(5))

