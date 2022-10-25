num = int(input())
temp = num
rev = 0
while num > 0:
    dig = num % 10  # to obtain last digit
    rev = rev * 10 + dig  # to print reverse number
    num = num // 10  # to obtain number other than last digit
if temp == rev:
    print("Is palindrome")
else:
    print("not a palindrome")
