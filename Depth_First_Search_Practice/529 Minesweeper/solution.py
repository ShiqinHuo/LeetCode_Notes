class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        h, w = len(board), len(board[0])

        def detect_neighbours(y, x, updated):
            c = 0
            neighbours = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1), (y + 1, x + 1), (y + 1, x - 1),
                          (y - 1, x + 1), (y - 1, x + 1)]
            valid_neighbours = [(i, j) for (i, j) in neighbours if (0 <= i < h) and (0 <= j < w)]
            for i, j in valid_neighbours:
                if 0 <= i < w and 0 <= j < h:
                    if board[i][j] == "M":
                        c += 1

            if c != 0: board[y][x] == str(c)
            if c == 0: board[y][x] == "B"
            updated.append((y, x))

            for i, j in valid_neighbours:
                if (i, j) not in updated:
                    detect_neighbours(i, j, updated)

        if 0 <= click[0] < h and 0 <= click[1] < w:
            if board[click[0]][click[1]] == "M":
                board[click[0]][click[1]] = "X"
            if board[click[0]][click[1]] == "E":
                detect_neighbours(click[0], click[1], [])
        return board