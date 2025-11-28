import matplotlib.pyplot as plt
import math

def generate_koch_polygon(n):
    sqrt3 = math.sqrt(3.0)
    poly = [(0.0, 0.0), (10.0, 0.0), (5.0, 5.0 * sqrt3), (0.0, 0.0)]
    for _ in range(n):
        new_poly = []
        for i in range(len(poly) - 1):
            x1, y1 = poly[i]
            x2, y2 = poly[i + 1]
            dx = (x2 - x1) / 3.0
            dy = (y2 - y1) / 3.0

            p1 = (x1, y1)
            p2 = (x1 + dx, y1 + dy)
            p3 = (x1 + 2.0 * dx, y1 + 2.0 * dy)

            angle = -math.pi / 3.0
            sx = math.cos(angle) * dx - math.sin(angle) * dy
            sy = math.sin(angle) * dx + math.cos(angle) * dy
            p4 = (p2[0] + sx, p2[1] + sy)

            new_poly.extend([p1, p2, p4, p3])
        new_poly.append(new_poly[0])
        poly = new_poly
    return poly

# Visualize K_n and lattice points
def visualize(d, n):
    poly = generate_koch_polygon(n)
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    p_min = math.ceil(xmin/d)
    p_max = math.floor(xmax/d)
    q_min = math.ceil(ymin/d)
    q_max = math.floor(ymax/d)

    lattice_x = []
    lattice_y = []
    for p in range(p_min, p_max+1):
        for q in range(q_min, q_max+1):
            lattice_x.append(p*d)
            lattice_y.append(q*d)

    plt.figure(figsize=(6,6))
    plt.scatter(lattice_x, lattice_y, s=10)
    plt.plot(xs, ys, color='black')
    plt.gca().set_aspect('equal')
    plt.title(f"Lattice points and Koch snowflake K_{n}")
    plt.show()

visualize(1.0, 2)