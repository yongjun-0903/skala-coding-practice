n = int(input())
t = []  
p = []

for _ in range(n):
    a, b = map(int, input().split())  
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)

for i in range(n):
    if i + t[i] <= n:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])