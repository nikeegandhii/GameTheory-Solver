import pandas as pd                     # Used to print the Matrix
from sympy import symbols, Eq, solve    # Used to calculate the Probability

# Format a Cell of the Matrix
def format_cell(cell, cell_index, result_value):
    return ("→" if result_value == "eq" or result_value == cell_index else "") + cell

# Format the values of the Matrix in order to output them
def format_matrix(matrix, result = None):
    if result == None:
        return [[str(matrix[0][0]) + ", " + str(matrix[0][1]),
                 str(matrix[1][0]) + ", " + str(matrix[1][1])],
                [str(matrix[2][0]) + ", " + str(matrix[2][1]),
                 str(matrix[3][0]) + ", " + str(matrix[3][1])]]
    else:
        return [[format_cell(str(matrix[0][0]), 0, result[0]) + ", " + format_cell(str(matrix[0][1]), 0, result[2]),
                 format_cell(str(matrix[1][0]), 0, result[1]) + ", " + format_cell(str(matrix[1][1]), 1, result[2])],
                [format_cell(str(matrix[2][0]), 1, result[0]) + ", " + format_cell(str(matrix[2][1]), 0, result[3]),
                 format_cell(str(matrix[3][0]), 1, result[1]) + ", " + format_cell(str(matrix[3][1]), 1, result[3])]]

# Print the Matrix on the screen
def print_matrix(players, headers, matrix, result = None):
    matrix_display = format_matrix(matrix, result)

    row_header = pd.MultiIndex.from_tuples([(players[0], headers[0]), (players[0], headers[1])])
    col_header = pd.MultiIndex.from_tuples([(players[1] + " " * 2, headers[0]), (players[1] + " " * 2, headers[1])])

    print(pd.DataFrame(matrix_display, col_header, row_header))

# Calculate which value to highlight in the Matrix
def calc_matrix(matrix):
    return [
        "eq" if matrix[0][0] == matrix[2][0] else (0 if matrix[0][0] > matrix[2][0] else 1),
        "eq" if matrix[1][0] == matrix[3][0] else (0 if matrix[1][0] > matrix[3][0] else 1),
        "eq" if matrix[0][1] == matrix[1][1] else (0 if matrix[0][1] > matrix[1][1] else 1),
        "eq" if matrix[2][1] == matrix[3][1] else (0 if matrix[2][1] > matrix[3][1] else 1)
    ]

# Calculate the Probability of a selected Player based on the Matrix
def calc_probability(matrix, player):
    player = 0 if player == 1 else 1

    P = symbols('P')
    equation = Eq(matrix[0][player] * P + matrix[2][player] * (1 - P) - matrix[1][player] * P - matrix[3][player] * (1 - P), 0)

    return solve(equation, P)[0]

# Main function where the execution of the program starts
if __name__ == "__main__":
    # Define the variables to hold the Players, the Decisions, and the values of the Matrix
    players = []
    headers = []
    matrix = []

    # Input the two Players
    print("Input the two Players")
    players.append(input("First Player: "))
    players.append(input("Second Player: "))

    # Input the two possible Decisions
    print("\nInput the two Decisions:")
    headers.append(input("First Decision: "))
    headers.append(input("Second Decision: "))

    # Input the Matrix, each row has a Cell in the Matrix
    print("\nInput the Matrix:")
    for cell in range(4):
        input_text = "Cell - " + ("Top" if cell < 2 else "Bottom") + ", " + ("Left" if cell % 2 == 0 else "Right") + ": "
        matrix.append(list(map(int, input(input_text).rstrip().split())))

    # Print the initial state of the Matrix
    print("\nInitial matrix:")
    print_matrix(players, headers, matrix)

    # Calculate the result of the Matrix and print its state
    result_matrix = calc_matrix(matrix)
    print("\nResulting matrix:")
    print_matrix(players, headers, matrix, result_matrix)

    # Calculate the probability of the First and Second Player
    print("\nProbability of the Players")
    print("Probability of " + players[0] + " being " + headers[0] + ": " + str(calc_probability(matrix, 0)))
    print("Probability of " + players[0] + " being " + headers[1] + ": " + str(1 - calc_probability(matrix, 0)))
    print("Probability of " + players[1] + " being " + headers[0] + ": " + str(calc_probability(matrix, 1)))
    print("Probability of " + players[1] + " being " + headers[1] + ": " + str(1 - calc_probability(matrix, 1)))