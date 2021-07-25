def number_of_diagonals(matrix: list) -> int:
    diagonals = 0
    for entry in matrix:
        if entry != 0:
            diagonals += 1
    return diagonals

def display(matrix: list) -> None:
    for i in range(len(matrix)):
        if i % 5 == 0:
            print()
        print(matrix[i], end=" ")

def is_valid(matrix: list) -> bool:
    if (matrix[-1] == 1): # /
        if (len(matrix) > 5) and (matrix[-6] == 2): # check upper cell
            return False
        if (len(matrix) > 5) and (len(matrix) % 5 != 0) and (matrix[-5] == 1): # check right upper cell
            return False
        if (len(matrix) % 5 != 1) and (matrix[-2] == 2): # check left cell
            return False
    elif matrix[-1] == 2: # \
        if (len(matrix) > 5) and (len(matrix) % 5 != 1) and (matrix[-7] == 2): # check left upper cell
            return False
        if (len(matrix) > 5) and (matrix[-6] == 1): # check upper cell
            return False
        if (len(matrix) % 5 != 1) and (matrix[-2] == 1): # check left cell
            return False
    else:
        return True
    return True

def fill_matrix(matrix: list):
    if len(matrix) == 25:
        if number_of_diagonals(matrix) == 16:
            display(matrix)
            print()
        return
    
    for line_type in [1, 2, 0]: # 1: /, 2: \, 0: no line
        matrix.append(line_type)
        if is_valid(matrix):
            fill_matrix(matrix)
        matrix.pop()

if __name__ == "__main__":
    fill_matrix(matrix=[])