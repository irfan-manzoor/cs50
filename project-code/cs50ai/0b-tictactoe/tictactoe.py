import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X, O]:
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(cell == player for cell in board[i]):
                return player
            if all(board[j][i] == player for j in range(3)):
                return player
        if board[0][0] == board[1][1] == board[2][2] == player:
            return player
        if board[0][2] == board[1][1] == board[2][0] == player:
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    curr_player = player(board)
    if curr_player == X:
        return max_action(board)[1]
    else:
        return min_action(board)[1]


def max_action(board):
    """
    Helper function for maximizing player (X).
    """
    if terminal(board):
        return utility(board), None

    max_utility = -math.inf
    best_action = None
    for action in actions(board):
        new_utility = min_action(result(board, action))[0]
        if new_utility > max_utility:
            max_utility = new_utility
            best_action = action
    return max_utility, best_action


def min_action(board):
    """
    Helper function for minimizing player (O).
    """
    if terminal(board):
        return utility(board), None

    min_utility = math.inf
    best_action = None
    for action in actions(board):
        new_utility = max_action(result(board, action))[0]
        if new_utility < min_utility:
            min_utility = new_utility
            best_action = action
    return min_utility, best_action
