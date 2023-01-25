# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
    print(i, end=" ")
    i += 1
print()

# break and continue statements works same as always

i = 1
while i < 6:
    print(i, end=" ")
    if i == 3:
        break
    i += 1

print()
# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")
print()
