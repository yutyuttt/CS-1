a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# 1
if a >= 100 and b <= 50:
    output = 1
else:
    output = 0

print(output)

# 2
if (a >= 100 and b <= 50) or (a <= 50 and b >= 100):
    output = 1
else:
    output = 0

print(output)