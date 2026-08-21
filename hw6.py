def p(w):
    p = 3

    if w > 5:
        p += (w - 2) * 3
    elif w <= 5 and w >= 2:
        p += (w - 2) * 2

    return p

print(p(4))
print(p(11))

w = int(input("Enter a number: "))
print(p(w))