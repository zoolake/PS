class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        def dfs(i, j):
            if  i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[i]) or \
                        grid[i][j] == '0':
                return
            
            grid[i][j] = '0'  # 방문처리
            dfs(i, j+1)     # 동
            dfs(i, j-1)     # 서
            dfs(i+1, j)     # 남
            dfs(i-1, j)     # 북

        result = 0
        # 순회
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1 # dfs 종료 후 육지 갯수 1 증가
        
        return result
