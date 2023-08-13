# wopop qeABt
# 11911111211 1131016566116

s = input()
d = {}
ans = ""
for i in s:
    if i.isalpha():
        if i in d:
            d[i] += 1
            ans += str(d[i]-1)
        else:
            d[i] = 1
            ans += str(ord(i))
    else:
        ans += i

print(ans)