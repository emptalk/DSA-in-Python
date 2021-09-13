
# can be optimized by dp
def ed(s1, s2, m, n):
	if m == 0:
		return n
	if n == 0:
		return m

	if s1[m-1] == s2[n-1]:
		return ed(s1, s2, m-1, n-1)
	else:
		return 1 + min(ed(s1, s2, m, n-1),\
					   ed(s1, s2, m-1, n),\
					   ed(s1, s2, m-1, n-1))


print(ed("SATURDAY", "SUNDAY", 8, 6))
