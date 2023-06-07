"""Main module to run the program."""


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    return board

def lista_de_elementos_repetidos(lista: list[int]) -> bool:
    lista = [x for x in lista if x != 0]
    return len(lista) != len(set(lista))

def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    for linha in board:
        # verifica se tem algum elemento repetido na linha
        if lista_de_elementos_repetidos(linha):
            return False
            #raise ValueError('Sudoku impossível de resolver')
        # verifica se o sudoku esta com algum elemento vazio
        if len(linha) != 9:
            return False
            #raise ValueError('Sudoku impossível de resolver')
    for j in range(len(board)):
        # j é o índice da coluna
        colunm = [linha[j] for linha in board]
        # verifica se tem algum elemento repetido na coluna
        if lista_de_elementos_repetidos(colunm):
            return False
            #raise ValueError('Sudoku impossível de resolver')
    return True

sudoku_board = [[1 for x in range(9)] for y in range(9)]

print(is_valid(sudoku_board))