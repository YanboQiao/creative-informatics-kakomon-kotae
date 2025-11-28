import math

def koch_snowflake_vertices(n: int) -> list[tuple[float, float]]:
    # 初始：逆时针三角形
    sqrt3 = math.sqrt(3.0)
    poly: list[tuple[float, float]] = [
        (0.0, 0.0),
        (10.0, 0.0),
        (5.0, 5.0 * sqrt3),
    ]

    for _ in range(n):
        new_poly: list[tuple[float, float]] = []
        m = len(poly)
        for i in range(m):
            x1, y1 = poly[i]
            x5, y5 = poly[(i + 1) % m]

            dx = (x5 - x1) / 3.0
            dy = (y5 - y1) / 3.0

            # 三等分点
            x2 = x1 + dx
            y2 = y1 + dy
            x4 = x1 + 2.0 * dx
            y4 = y1 + 2.0 * dy

            # 逆时针多边形要向外凸出：旋转 -60°
            angle = -math.pi / 3.0
            cosa = math.cos(angle)
            sina = math.sin(angle)
            rx = cosa * dx - sina * dy
            ry = sina * dx + cosa * dy

            x3 = x2 + rx
            y3 = y2 + ry

            # 每条边替换为 4 段：P1 -> P2 -> P3 -> P4
            new_poly.extend([
                (x1, y1),
                (x2, y2),
                (x3, y3),
                (x4, y4),
            ])

        poly = new_poly

    # 此时 poly 是逆时针，转成顺时针且不重复起点
    if len(poly) <= 1:
        return poly
    vertices_cw: list[tuple[float, float]] = [poly[0]] + list(reversed(poly[1:]))
    return vertices_cw

def is_in_Koch(vertices: list[tuple[float, float]], point: tuple[float, float]) -> bool:
    eps = 1e-9
    x, y = point
    inside = False
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        if point_on_segment(vertices[i], vertices[(i + 1) % n], point):
            return True
        if (x1 > x) == (x2 > x):
            continue
        y_kouten = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
        if y_kouten > y:
            inside = not inside
            
    return inside

def point_on_segment(hajime: tuple[float, float], owari: tuple[float, float], ten: tuple[float, float]) -> bool:
    eps = 1e-9
    x1, y1 = hajime
    x2, y2 = owari
    x, y = ten
    cross_product = (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)
    if abs(cross_product) > eps:
        return False
    if x < min(x1, x2) - eps or x > max(x1, x2) + eps:
        return False
    if y < min(y1, y2) - eps or y > max(y1, y2) + eps:
        return False
    return True

def getpoints(hiritsu: float) -> list[list[tuple[float, float]]]:
    shita_boundary = -3.0
    ue_boundary = 10.0
    hidari_boundary = 0.0
    migi_boundary = 10.0

    p_min = math.ceil(hidari_boundary / hiritsu)
    p_max = math.floor(migi_boundary / hiritsu)
    q_min = math.ceil(shita_boundary / hiritsu)
    q_max = math.floor(ue_boundary / hiritsu)

    rows = []
    for q in range(q_min, q_max + 1):
        y = q * hiritsu
        row = []
        for p in range(p_min, p_max + 1):
            x = p * hiritsu
            row.append((x, y))
        rows.append(row)

    return rows

def main():
    d = 1
    n = 1
    points = getpoints(d)
    vertices = koch_snowflake_vertices(n)
    count: int = 0
    for row in points:
        for point in row:
            if is_in_Koch(vertices, point):
                count += 1
    print(count)

if __name__ == "__main__":
    main()