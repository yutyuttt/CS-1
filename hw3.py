# 1
val = 10
while val <= 37:
    print(val, end=" ")
    val += 3

print()

# 2 
val = 998
while val >= 900:
    print(val, end=" ")
    val -= 2

print()

# 3
for i in range(0, 20):
    if i % 2 == 0:
        output = 1
    else:
        output = -1
    print(output, end=" ")

print()

# 4
for i in range(1, 61):
    output = 7
    if i % 3 == 0:
        output = 9
    print(output, end=" ")