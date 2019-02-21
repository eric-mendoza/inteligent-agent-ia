#  Universidad del Valle de Guatemala
#  Inteligencia Artificial
#  Eric Mendoza: 15002
#  Proyecto 1: Agente inteligente
#  Puzzle15.py: El presente programa implementa el algoritmo A* para solucionar el 15 puzzle


def main():
    print("Ingrese la cadena de puzzle que desea resolver:")
    raw_puzzle = "F21C856B49A73ED"  # input()
    puzzle = format_input(raw_puzzle)
    print(print_puzzle(puzzle))
    print("Se ejecutaron los siguientes pasos:")


def format_input(raw_puzzle):
    puzzle = [[], [], [], []]
    if len(raw_puzzle) != 15:
        print("Se ha ingresado un puzzle incorrecto.")
        exit(-1)

    raw_puzzle += " "  # Agregar espacio vacio.

    index = 0
    for i in range(4):
        for j in range(4):
            value = raw_puzzle[index]
            if value == "A":
                value = 10
            elif value == "B":
                value = 11
            elif value == "C":
                value = 12
            elif value == "D":
                value = 13
            elif value == "E":
                value = 14
            elif value == "F":
                value = 15
            elif value == " ":
                value = "."
            else:
                value = int(value)
            puzzle[i].append(value)
            index += 1

    return puzzle


def print_puzzle(puzzle):
    result = "╔═══════╤══════╤═══════╤═══════╗\n"
    result += "║\t%s\t│\t%s\t│\t%s\t│\t%s\t║\n" % (puzzle[0][0], puzzle[0][1], puzzle[0][2], puzzle[0][3])
    result += "╟───────┼──────┼───────┼───────╢\n"
    result += "║\t%s\t│\t%s\t│\t%s\t│\t%s\t║\n" % (puzzle[1][0], puzzle[1][1], puzzle[1][2], puzzle[1][3])
    result += "╟───────┼──────┼───────┼───────╢\n"
    result += "║\t%s\t│\t%s\t│\t%s\t│\t%s\t║\n" % (puzzle[2][0], puzzle[2][1], puzzle[2][2], puzzle[2][3])
    result += "╟───────┼──────┼───────┼───────╢\n"
    result += "║\t%s\t│\t%s\t│\t%s\t│\t%s\t║\n" % (puzzle[3][0], puzzle[3][1], puzzle[3][2], puzzle[3][3])
    result += "╚═══════╧══════╧═══════╧═══════╝\n"
    return result


main()
