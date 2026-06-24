# 79. Word Search - medium
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
            Given an m * n grid of chars board and string word
            Return True if word exists in the grid

            A path is valid if the word can be constructed of sequentially adjacent letters where the adjacent cells are horizontal or vertical neighbors.
            Same cells cannot be used more than once in the path.

            Constraints:
              - 1 <= m, n <= 6
              - 1 <= word.length <= 15
              - letters in the cells are lowercase and uppercase English letters

            Edge cases:
              - Single cell board
              - word is longer than the total cells

            Observations:
              - word cannot be empty
              - board cannot be empty

            We first can check the edge case where the word length is greater than the amount of total cells to see if it's even possible. Then we can iterate through each cell and call a DFS function at each valid starting letter. The DFS function will return a boolean to see if the word is in the board. Then we'll check neighboring cells, and mark each cell in path as seen. If the path is invalid, we'll backtrack and unmark the cells for a search of another path.
        '''
        def dfs(board, i, j, m, n, letter_index, seen = None):
            if letter_index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if seen is None:
                seen = set()

            if (i, j) in seen:
                return False

            if board[i][j] == word[letter_index]:
                seen.add((i, j))

                res = (dfs(board, i+1, j, m, n, letter_index+1, seen) or \
                      dfs(board, i-1, j, m, n, letter_index+1, seen) or \
                      dfs(board, i, j+1, m, n, letter_index+1, seen) or \
                      dfs(board, i, j-1, m, n, letter_index+1, seen))

                seen.remove((i, j))

                return res

            return False

        m = len(board)
        n = len(board[0])

        if len(word) > m*n:
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, m, n, 0):
                        return True

        return False

    # O(m * n * 4^L) time, O(m*n) or O(L) space
