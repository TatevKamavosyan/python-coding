import matplotlib.pyplot as plt

# Ուղղանկյան տվյալներ
x, y = 2, 3
z,h = 5, 4

# Գագաթների կոորդինատներ

xs = [1,2, 4, 3, 1]
ys = [1, 3, 2, 0,1]

# Գծագրում
plt.figure(figsize=(6, 6))
plt.plot(xs, ys, marker='o')
plt.fill(xs, ys, alpha=0.2)

# Առանցքներ
plt.axhline(0)
plt.axvline(0)

# Կարգավորումներ
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Ուղղանկյան վիզուալիզացիա")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
