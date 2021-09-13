def lis(arr, n):
	# aux space: O(n)
	tail = [None for _ in range(n)]
	len = 1

	tail[0] = arr[0]

	# time: O(nlogn)
	for i in range(1, n):
		if arr[i] > tail[len-1]:
			tail[len] = arr[i]
			len += 1
		else:
			c = ceilIdx(tail, 0, len-1, arr[i])
			tail[c] = arr[i]

	return len

# time: O(logn)
def ceilIdx(tail, l, r, x):
	while r > l:
		m = l + int((r-l)/2) # mid point
		if tail[m] >= x:
			r = m
		else:
			l = m + 1
	return r


print(lis([3, 10, 20, 4, 6, 7], 6))