import matplotlib.pyplot as plt

# Create two related lists: x values and their squares
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [i**2 for i in x]

plt.scatter(x, y)
plt.xlabel("x value")
plt.ylabel("x squared")
plt.title("Scatter Plot of x vs x squared")
plt.show()