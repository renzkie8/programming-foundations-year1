x = 15
y = 13
result = 0
while x > 0:
    if x % 2 == 1:
        result += y
    x = x // 2  # Update the value of x by integer division
    y *= 2
print(result)
