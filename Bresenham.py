import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []  # store all points on the line
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points


# Example: Draw line from (2, 3) to (15, 10)
points = bresenham_line(2, 3, 15, 10)

# Plot the line
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

plt.figure(figsize=(6, 6))
plt.title("Bresenham Line Drawing Algorithm")
plt.plot(x_coords, y_coords, marker='s', color='blue', linestyle='-', markersize=8)
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
