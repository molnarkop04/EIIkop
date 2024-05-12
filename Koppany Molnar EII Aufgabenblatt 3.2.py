def g(a, b, c, d):
    return (not a and not b and not c and d) or (not a and b and not c and not d) or (not a and b and not c and d) or (not a and b and c and d) or (a and not b and c and not d) or (a and not b and c and d) or (a and b and not c and not d) or (a and b and not c and d) or (a and b and c and not d) or (a and b and c and d)


print(g(0, 0, 0, 1))
print(g(0, 1, 0, 0))
print(g(0, 1, 0, 1))
print(g(0, 1, 1, 1))
print(g(1, 0, 1, 0))
print(g(1, 0, 1, 1))
print(g(1, 1, 1, 0))
print(g(1, 1, 1, 1))