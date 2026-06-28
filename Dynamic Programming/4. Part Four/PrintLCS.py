length = dp[n][m]
ans = [''] * length

index = length - 1
i, j = n, m

while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        ans[index] = s[i - 1]
        index -= 1
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(''.join(ans))


# After doing lcs , do the above step 👆    