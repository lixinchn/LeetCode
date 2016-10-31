class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        second_left, third_left = 0, 0
        second_top, third_top = 0, 0

        if A <= E:
            if C <= E:
                return (C - A) * (D - B) + (G - E) * (H - F)
            elif C >= E and C <= G:
                second_left = E
                third_left = C
            else:
                second_left = E
                third_left = G
        elif A > E and A < G:
            if C <= G:
                second_left = A
                third_left = C
            else:
                second_left = A
                third_left = G
        else:
            return (C - A) * (D - B) + (G - E) * (H - F)

        if D >= H:
            if B >= H:
                return (C - A) * (D - B) + (G - E) * (H - F)
            elif B <= H and B >= F:
                second_top = B
                third_top = H
            else:
                second_top = F
                third_top = H
        elif D > F and D < H:
            if B >= F:
                second_top = B
                third_top = D
            else:
                second_top = F
                third_top = D
        else:
            return (C - A) * (D - B) + (G - E) * (H - F)


        return (C - A) * (D - B) + (G - E) * (H - F) - (third_left - second_left) * (third_top - second_top)

solution = Solution()
# print solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 6
# print solution.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
print solution.computeArea(-2,-2,2,2,1,1,3,3)


