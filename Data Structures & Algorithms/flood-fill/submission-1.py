class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        starting_color = image[sr][sc]
        def dfs(i, j):
            if i >= len(image) or j >= len(image[0]) or i < 0 or j < 0:
                return
            if (i,j) in visit:
                return
            visit.add((i,j))
            if image[i][j] == starting_color:
                image[i][j] = color
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
            return
        dfs(sr, sc)
        return image