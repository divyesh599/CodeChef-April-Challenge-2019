t = int(input())
ans = []

###################
for _ in range(t):
	n = int(input())
	s, s1 = map(str, input().split())

	temp = 0
	tm = -1
	for i in range(n):
		if s[i] == s1:
			tn = i - tm - 1
			temp = temp + tn * (tn + 1) // 2
			tm = i

	if s[-1] != s1:
		tn = n - tm - 1
		temp = temp + tn * (tn + 1) // 2
	tans = n * (n + 1) // 2

	ans.append(tans - temp)

###################
print(*ans, sep = '\n')