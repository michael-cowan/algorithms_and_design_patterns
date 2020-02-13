import sys
'''
Question:
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['M','B','K','E'],
  ['S','F','C','S'],
  ['A','D','E','E'],
  ['O','Q','R','S'],
]


Given word = "MBFDEE", return true.
Given word = "SEE", return true.
Given word = "ABEB", return false.

'''

board = [
  ['M', 'B', 'K', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E'],
  ['O', 'Q', 'R', 'S'],
]

word = 'SEE'

check = [(i, j) for i in range(-1, 2) for j in range(-1, 2)
         if bool(i) + bool(j) == 1]


def makes_word(r, c, wi, used):
    if wi == len(word):
        return True
    for add_r, add_c in check:
        nr, nc = r + add_r, c + add_c
        if (-1 < nr < len(board)
           and -1 < nc < len(board[0])
           and (nr, nc) not in used
           and board[nr][nc] == word[wi]):
            used.add((nr, nc))
            return makes_word(nr, nc, wi + 1, used)
    else:
        return False


wi = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == word[wi]:
            used = set([(r, c)])
            if makes_word(r, c, wi + 1, used):
                print('TRUE')
                sys.exit()
else:
    print('FALSE')
