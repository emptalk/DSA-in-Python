# recursive solution for knapsack
# T(n) = 2T(n-1) + theta(1)
# O(2^n)
def knapsack(W, wt, val, n):
	if n == 0 or W == 0:
		return 0

	if wt[n-1] > W: # can not add last item?
		return knapsack(W, wt, val, n-1)
	else:
		return max(knapsack(W, wt, val, n-1),
				   val[n-1] + knapsack(W-wt[n-1], wt, val, n-1))

# W, n is different for recursive call,
# so they are the axises for dp solution

res = knapsack(10, [5,4,6,3], [10, 40, 30, 50], 4)
print(res)