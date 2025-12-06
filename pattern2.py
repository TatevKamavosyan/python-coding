# Triangle pattern with numbers
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Star pattern
print("\n")
for i in range(1, n + 1):
    print("*" * i)

# Pyramid pattern
print("\n")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))