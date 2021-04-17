class Vector(object):
    def sum(self, vector1: list, vector2: list) -> list:
        sum_vector = []
        for v1_ele, v2_ele in zip(vector1, vector2):
            sum_vector.append(v1_ele + v2_ele)
        return sum_vector

    def difference(self, x: list, y: list) -> list:
        diff_vector = []
        for x_ele, y_ele in zip(x, y):
            diff_vector.append(x_ele - y_ele)
        return diff_vector

    def norm(self, vector: list) -> int:
        norm = 0
        for ele in vector:
            norm += ele ** 2
        return norm

    def dot_product(self, x: list, y: list) -> int:
        dot_product = 0
        for x_ele, y_ele in zip(x, y):
            dot_product += x_ele * y_ele
        return dot_product

    def epcilon(self, i: int, j: int, k: int) -> int:
        e = [
            [[0, 0, 0], [0, 0, 1], [0, -1, 0]],
            [[0, 0, -1], [0, 0, 0], [1, 0, 0]],
            [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]]
        return e[i][j][k]

    def cross_product(self, x: list, y: list) -> list:
        cross_product = []
        dimention = len(x)
        for i in range(dimention):
            element = 0
            for j in range(dimention):
                for k in range(dimention):
                    element += self.epcilon(i, j, k) * x[j] * y[k]
            cross_product.append(element)
        return cross_product

    def projection(self, p: list) -> list:
        xp = self.difference(p, self.x)
        xy = self.difference(self.y, self.x)

        dot_xp_xy = self.dot_product(xp, xy)
        norm_xy = self.norm(xy)

        k = dot_xp_xy / norm_xy
        X = []
        for ele_x, xy_ele in zip(self.x, xy):
            X.append(ele_x + k * xy_ele)

        return X

    def reflection(self, p: list) -> list:
        projection_point = self.projection(p)

        p_to_projection_point = self.difference(projection_point, p)
        ref_point = []
        for p_ele, p_to_pro_ele in zip(p, p_to_projection_point):
            ref_point.append(p_ele + 2 * p_to_pro_ele)

        return ref_point

    def distance(self, p: list) -> float:
        projection_point = self.projection(p)
        p_to_projection_point = self.difference(projection_point, p)
        return self.norm(p_to_projection_point)**(1 / 2)

    def line_equation(self, p1: list, p2: list, p3: list) -> float:
        # p1 -> [X1, Y1] p2 -> [X2, Y2] p3 -> [x, y]
        return (p3[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def intersection(self, p1: list, p2: list, p3: list, p4: list) -> bool:
        f1 = self.line_equation(p3, p4, p1)
        f2 = self.line_equation(p3, p4, p2)
        f3 = self.line_equation(p1, p2, p3)
        f4 = self.line_equation(p1, p2, p4)

        if f1 == f2 == 0:
            return False

        if f1 * f2 <= 0 and f3 * f4 <= 0:
            return True
        else:
            return False

    def cross_point(self, p1: list, p2: list, p3: list, p4: list) -> list:
        if not self.intersection(p1, p2, p3, p4):
            return

        p1_p2_vector = self.difference(p2, p1)
        p1_p3_vector = self.difference(p3, p1)
        p1_p4_vector = self.difference(p4, p1)

        S1 = self.norm(self.cross_product(
            p1_p2_vector, p1_p3_vector)) ** (1 / 2)
        S2 = self.norm(self.cross_product(p1_p2_vector, p1_p4_vector))**(1 / 2)

        p3_p4 = self.difference(p4, p3)
        X = []
        for p3_ele, p3_p2_ele in zip(p3, p3_p4):
            element = p3_ele + (S2 / (S1 + S2)) * p3_p2_ele
            X.append(element)

        return X


if __name__ == "__main__":
    x = [-1, 0]
    y = [-1, -10]
    vector = Vector(x, y)
    print(vector.cross_point([0, 0, 0], [1, 1, 0], [1, 0, 0], [0, 1, 0]))
