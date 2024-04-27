lower_value = int(input("Enter the lower value: "))
upper_value = int(input("Enter the upper value: "))
for i in range(lower_value,upper_value+ 1):
    q = 0
    n = i
    while n > 0:
        digit = n % 10
        q += digit ** 3
        n //= 10
        if i == q:
            print(i)
