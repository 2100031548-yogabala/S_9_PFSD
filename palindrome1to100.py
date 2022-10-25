d = 0
rev = 0
for i in range (1, 101):
    n = i
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = int(n / 10)
    if i == rev:
        print(i)
    rev=0

