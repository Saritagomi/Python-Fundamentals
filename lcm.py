def lcm(a, b):
    if (b == 0):
        return a;
    else:
        return lcm(b, a % b)


num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

gcd = lcm(num1, num2)
print("Gcd of {0} and {1} ={2}".format(num1,num2,gcd))

res = (num1 * num2) / gcd
print(" LCM of {0} and {1} = {2}".format(num1, num2, res))