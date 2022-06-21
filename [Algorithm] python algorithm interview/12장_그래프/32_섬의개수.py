# https://leetcode.com/problems/number-of-islands

# DFS 이용
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = 0

        def find(r, c):
            for i in range(4):
                nr, nc = r + moves[i][0], c + moves[i][1]
                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])
                    and grid[nr][nc] == "1"
                ):
                    grid[nr][nc] = "0"
                    find(nr, nc)
                else:
                    continue
            return None

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    find(r, c)
                    result += 1

        return result
