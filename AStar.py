#  Universidad del Valle de Guatemala
#  Inteligencia Artificial
#  Eric Mendoza: 15002
#  Proyecto 1: Agente inteligente
#  AStar.py: El presente archivo ejecuta una version generica de A*

from queue import PriorityQueue


class State(object):
    def __init__(self, state, parent, start=0, goal=0):
        self.frontier = []  # Contendra los estados que se pueden alcanzar desde este estado
        self.parent = parent  # Del estado desde el que se vino a este estado
        self.state = state  # El presente estado (sudoku/puzzle)
        self.total_cost = 0  # f() = path_cost(path) + heuristic(path.end)
        if parent:
            self.path = parent.path[:]
            self.path.append(state)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [state]
            self.start = start  # Deberia ser el sudoku/puzzle inicial
            self.goal = goal  # Se busca que queden 0 casillas vacias

    def get_total_cost(self):  # f() = path_cost(path) + heuristic(path.end)
        pass

    def generate_frontier(self):
        pass


class StateString(State):
    def __init__(self, state, parent, start=0, goal=0):
        super(StateString, self).__init__(state, parent, start, goal)
        self.total_cost = self.get_total_cost()  # Calcular el costo de la ruta

    def get_total_cost(self):
        total_cost = 0
        for k in range(len(self.goal)):
            letter = self.goal[k]
            total_cost += abs(k - self.state.index(letter))
        return total_cost

    def generate_frontier(self):
        if not self.frontier:
            # Actions: Las acciones que se pueden tomar a partir de un estado
            for i in range(len(self.goal) - 1):
                val = self.state
                val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
                child = StateString(val, self)
                self.frontier.append(child)


class AStarSolver:
    def __init__(self, start, goal, goal_test):
        self.path = []  # Contendra el reccorrido final de estados recorridos
        self.visitedQueue = []  # Contiene los estados explorados
        self.frontier = PriorityQueue()  # Contiene los estados de frontera en orden de prioridad segun heuristica
        self.start = start  # Contiene el estado inicial
        self.goal = goal  # Contiene el estado al que se busca llegar
        self.goal_test = goal_test  # Funcion que evalua si ya se llego al resultado

    def solve(self):
        start_state = StateString(self.start, 0, self.start, self.goal)
        count = 0

        # Iniciar la priority queue en el estado inicial. Se le agrega la tupla (heuristica, contador, estado)
        self.frontier.put((0, count, start_state))

        # Ejecutar hasta que se tenga una solucion o hasta que se acaben los estados de frontera
        while not self.path and self.frontier.qsize():
            closest_child = self.frontier.get()[2]  # Obtiene el estado con mas prioridad
            closest_child.generate_frontier()
            print(closest_child.state)
            self.visitedQueue.append(closest_child.state)  # Agregar el estado actual a los estados visitados.

            # Agregar los nuevos estados frontera al listado de frontera general
            for child in closest_child.frontier:
                if child.state not in self.visitedQueue:
                    count += 1
                    # Funcion goal_test
                    if self.goal_test(child):  # Sera cero si es el estado final que se busca
                        self.path = child.path
                        break
                    self.frontier.put((child.total_cost, count, child))
        if not self.path:
            print("Problema no tiene solucion.")
        return self.path


if __name__ == "__main__":
    start1 = "arodatupmoc"
    goal1 = "computadora"
    print("Starting...")

    # Implementacion de A*
    def goal_test1(state):
        return state.state == state.goal

    a = AStarSolver(start1, goal1, goal_test1)
    a.solve()
    for i in range(len(a.path)):
        print("%d) " % i + a.path[i])
