"""Main module to run the program."""

def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    # Procurar uma célula vazia
    i, j = find_empty(board)
    # Se nao houver célula vazia, sudoku resolvido
    if i == None or j == None:
      return board
    # testa todos os valores que são possíveis
    for valorTeste in range(1,10):
      # substitui o valor vazio para teste
      board[i][j] = valorTeste
      # testa se é um opção válida
      if is_valid(board):
        # executa novamente
        solve_sudoku(board)
      board[i][j] = 0
    

def find_empty(board: list[list[int]]) -> tuple:
    for i in range(9):
      for j in range(9):
        if board[i][j] == 0:
          return i, j
    return None, None

def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    # para cada linha i do tabuleiro
    for i in range(9):
      # para cada coluna j do tabuleiro
      for j in range(9):
        # Guarda o valor do elemento board[i][j]
        numTeste = board[i][j]
        if numTeste != 0:
          # Procurar um mesmo valor nas colunas diferentes
          for col in range(9):
            if col != j and board[i][col] == numTeste:
              return False

          # Procurar um mesmo valor nas linhas diferentes
          for line in range(9):
            if line != i and board[line][j] == numTeste:
              return False

          # variavel que define os setores
          line_vetor = 3 * (i//3)
          col_vetor = 3 * (j//3)
          # para cada elemento na linha do vetor
          for Ai in range(line_vetor,line_vetor + 3):
            # para cada elemento na coluna do vetor
            for Aj in range(col_vetor, col_vetor + 3):
              # testa se outro elemento do vetor é igual ao elemento de teste
              if (Ai != i or Aj != j) and board[Ai][Aj] == numTeste:
                return False
    return True
