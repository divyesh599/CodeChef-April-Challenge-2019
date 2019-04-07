## https://www.codechef.com/APRIL19B/problems/MAXREM/

n = int(input())
ans = 0
a = list(map(int, input().split()))

a.sort(reverse=True)

m = a[0]

for i in range(1,n):
	if m != a[i]:
		ans = a[i]
		break
print(ans)
