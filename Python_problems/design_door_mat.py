n, m = map(int, input().split())

# Upper part
for i in range(n // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, "-"))

# Center
print("WELCOME".center(m, "-"))

# Lower part
for i in range(n // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, "-"))
