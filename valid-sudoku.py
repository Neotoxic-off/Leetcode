class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        i = 0
        j = 0
        blocks = []

        while i < (len(board)):
            while j < (len(board[i])):
                block = self.__extract_block__(board, i, j)
                if (self.__check_block__(block) == True):
                    blocks.append(block)
                else:
                    return False
                j += 3
            i += 3
            j = 0
        for b in range(len(blocks)):
            if (self.__validate__(blocks, b) == False):
                return False

        return True
    
    def __validate__(self, blocks, block_position):
        f = []

        for i in range(len(blocks)):
            if (i != block_position):
                for number in blocks[block_position]:
                    if (number != '.'):
                        if (number in blocks[i]):
                            if (blocks[i].index(number) == blocks[block_position].index(number)):
                                f.append((blocks[block_position], blocks[i]))
        print(f)
        return True

    def __extract_block__(self, board, x, y):
        return (
            [
                board[x][y], board[x + 1][y], board[x + 2][y],
                board[x][y + 1], board[x + 1][y + 1], board[x + 2][y + 1],
                board[x][y + 2], board[x + 1][y + 2], board[x + 2][y + 2]
            ]
        )
    
    def __check_block__(self, block):
        for i in block:
            if (i != '.'):
                if (block.count(i) > 1):
                    return False
        return True

Solution().isValidSudoku([
    ["5","3",".",    ".","7",".",    ".",".","."],
    ["6",".",".",    "1","9","5",    ".",".","."],
    [".","9","8",    ".",".",".",    ".","6","."],

    ["8",".","."    ,".","6",".",    ".",".","3"],
    ["4",".",".",    "8",".","3",    ".",".","1"],
    ["7",".",".",    ".","2",".",    ".",".","6"],

    [".","6",".",    ".",".",".",    "2","8","."],
    [".",".",".",    "4","1","9",    ".",".","5"],
    [".",".",".",    ".","8",".",    ".","7","9"]
])

# Solution().isValidSudoku([
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ])