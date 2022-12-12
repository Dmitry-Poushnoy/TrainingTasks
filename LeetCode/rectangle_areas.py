class Solution:
    def compute_area(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int | None:
        @staticmethod
        def set_cells(ax1, ay1, ax2, ay2) -> set[tuple[int, int]]:
            """ Calc amount of 1x1 cells in rectangle"""
            cells = set()
            for x in range(ax1, ax2):
                for y in range(ay1, ay2):
                    cells.add((x, y))
            return cells


if __name__ == '__main__':
    s = Solution()
    print(s.compute_area(-2, -2, 2, 2, 1, 1, 3, 3))
