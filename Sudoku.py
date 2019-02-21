#  Universidad del Valle de Guatemala
#  Inteligencia Artificial
#  Eric Mendoza: 15002
#  Proyecto 1: Agente inteligente
#  Sudoku.py: El presente programa implementa el algoritmo A* para solucionar Sudokus de 4x4


def main():
    print("Ingrese la cadena de Sudoku que desea resolver:")
    raw_sudoku = ".4.13.4.1..4.21."  # input()
    sudoku = format_input(raw_sudoku)
    print(print_sudoku(sudoku))
    print("Se ejecutaron los siguientes pasos:")


def format_input(raw_sudoku):
    sudoku = [[], [], [], []]
    if len(raw_sudoku) != 16:
        print("Se ha ingresado un sudoku incorrecto.")
        exit(-1)

    index = 0
    for i in range(4):
        for j in range(4):
            sudoku[i].append(raw_sudoku[index])
            index += 1

    return sudoku


def print_sudoku(sudoku):
    result = "╔═══╤═══╦═══╤═══╗\n"
    result += "║ %s │ %s ║ %s │ %s ║\n" % (sudoku[0][0], sudoku[0][1], sudoku[0][2], sudoku[0][3])
    result += "╟───┼───╫───┼───╢\n"
    result += "║ %s │ %s ║ %s │ %s ║\n" % (sudoku[1][0], sudoku[1][1], sudoku[1][2], sudoku[1][3])
    result += "╠═══╪═══╬═══╪═══╣\n"
    result += "║ %s │ %s ║ %s │ %s ║\n" % (sudoku[2][0], sudoku[2][1], sudoku[2][2], sudoku[2][3])
    result += "╟───┼───╫───┼───╢\n"
    result += "║ %s │ %s ║ %s │ %s ║\n" % (sudoku[3][0], sudoku[3][1], sudoku[3][2], sudoku[3][3])
    result += "╚═══╧═══╩═══╧═══╝\n"
    return result


main()
