#!/usr/bin/python3
"""To solve the N-queens puzzle."""
import sys


def init_brd(n):
    """To nitialize an `n`x`n` sized chessboard with 0's."""
    brd = []
    [brd.append([]) for q in range(n)]
    [row.append(' ') for q in range(n) for row in brd]
    return (brd)


def brd_deepcopy(brd):
    """To return a chessboard's deepcopy."""
    if isinstance(brd, list):
        return list(map(brd_deepcopy, brd))
    return (brd)


def get_solution(brd):
    """To represent a solved chessboard."""
    solution = []
    for v in range(len(brd)):
        for c in range(len(brd)):
            if brd[v][c] == "Q":
                solution.append([v, c])
                break
    return (solution)


def xout(brd, row, col):
    """Xes out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played to be X-ed out.

    Args:
        brd (list): The current working chessboard.
        row (int): The queen's last play on the row.
        col (int): The queen's last play on the column.
    """
    # X out all forward spots on the brd
    for c in range(col + 1, len(brd)):
        brd[row][c] = "x"
    # X out all backwards spots on the brd
    for c in range(col - 1, -1, -1):
        brd[row][c] = "x"
    # X out all spots on the brd below
    for v in range(row + 1, len(brd)):
        brd[v][col] = "x"
    # X out all spots above the brd
    for v in range(row - 1, -1, -1):
        brd[v][col] = "x"
    # X out all spots diagonally down to the right of the brd
    c = col + 1
    for v in range(row + 1, len(brd)):
        if c >= len(brd):
            break
        brd[v][c] = "x"
        c += 1
    # X out all spots diagonally up to the left of the brd
    c = col - 1
    for v in range(row - 1, -1, -1):
        if c < 0:
            break
        brd[v][c]
        c -= 1
    # X out all spots diagonally up to the right of the brd
    c = col + 1
    for v in range(row - 1, -1, -1):
        if c >= len(brd):
            break
        brd[v][c] = "x"
        c += 1
    # X out all spots diagonally down to the left of the brd
    c = col - 1
    for v in range(row + 1, len(brd)):
        if c < 0:
            break
        brd[v][c] = "x"
        c -= 1


def recursive_solve(brd, row, queens, solutions):
    """To solve an N-queens puzzle recursively.

    Args:
        board (list): current working chessboard.
        row (int): current working row.
        queens (int): current no. of placed queens.
        solutions (list): solutions.
    Returns:
        solutions
    """
    if queens == len(brd):
        solutions.append(get_solution(brd))
        return (solutions)

    for c in range(len(brd)):
        if brd[row][c] == " ":
            tmp_brd = brd_deepcopy(brd)
            tmp_brd[row][c] = "Q"
            xout(tmp_brd, row, c)
            solutions = recursive_solve(tmp_brd, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = init_brd(int(sys.argv[1]))
    solutions = recursive_solve(brd, 0, 0, [])
    for solt in solutions:
        print(solt)
