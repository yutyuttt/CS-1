val = int(input("Enter the value of your cards: "))

if val < 17:
    output = "Hit"
elif val > 21:
    output = "Bust"
else:
    output = "Stand"
print(output)