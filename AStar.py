#  Universidad del Valle de Guatemala
#  Inteligencia Artificial
#  Eric Mendoza: 15002
#  Proyecto 1: Agente inteligente
#  AStar.py: El presente archivo ejecuta una version generica de A*

from queue import PriorityQueue


# ACTION PARA CADA NODO
class State(object):
    def __init__(self, state, parent, action, start=0, goal=0):
        self.frontier = []  # Contendra los estados que se pueden alcanzar desde este estado
        self.parent = parent  # Del estado desde el que se vino a este estado
        self.state = state  # El presente estado (sudoku/puzzle)
        self.total_cost = 0  # f() = path_cost(path) + heuristic(path.end)
        self.action = ""  # Que accion creo este estado
        if parent:
            self.path = parent.path[:]  # Copia el path del padre
            self.path.append(self)  # Y se agrega a si mismo
            self.start = parent.start
            self.goal = parent.goal
            self.action = action
        else:
            self.path = [self]
            self.start = start  # Deberia ser el sudoku/puzzle inicial
            self.goal = goal  # Se busca que queden 0 casillas vacias
            self.action = "Inicio."

    def get_total_cost(self):  # f() = path_cost(path) + heuristic(path.end)
        pass

    def result(self, action):  # devuelve un nuevo estado a partir de una accion y un estado inicial
        pass

    def actions(self):  # Define que acciones se pueden realizar en el presente estado
        pass

    def goal_test(self):  # Determina si se ha llegado al fin del problema
        pass

    def get_path_cost(self):  # Calcula el costo de una ruta
        pass

    def get_step_cost(self):  # Devuelve el costo de moverse de un estado a otro (Siempre sera 1 en nuestro caso)
        pass

    def generate_frontier(self):
        pass


# Implementacion para ordenador de palabras
class StateString(State):
    def __init__(self, state, parent, action, start=0, goal=0):
        super(StateString, self).__init__(state, parent, action, start, goal)
        self.total_cost = self.get_total_cost()  # Calcular el costo de la ruta (heuristica + pathcost)

    # f() = path_cost(path) + heuristic(path.end)
    def get_total_cost(self):
        total_cost = 0
        for k in range(len(self.goal)):
            letter = self.goal[k]
            total_cost += abs(k - self.state.index(letter))
        return total_cost

    def generate_frontier(self):
        if not self.frontier:
            # Actions: Las acciones que se pueden tomar a partir de un estado
            actions = self.actions()
            for i in actions:
                action = self.state
                action = action[:i] + action[i + 1] + action[i] + action[i + 2:]
                child = self.result(action)
                self.frontier.append(child)

    def result(self, action):  # Devuelve un nuevo estado a partir de una accion
        return StateString(action, self, "SWIPE")

    def goal_test(self):
        return self.state == self.goal

    def get_path_cost(self):  # Calcula el costo de una ruta
        return len(self.path)

    def get_step_cost(self):  # Devuelve el costo de moverse de un estado a otro (Siempre sera 1 en nuestro caso)
        return 1

    def actions(self):  # Define que acciones se pueden realizar en el presente estado
        return range(len(self.goal) - 1)


class AStarSolver:
    def __init__(self, problem_state, start, goal):
        self.path = []  # Contendra el reccorrido final de estados recorridos
        self.visitedQueue = []  # Contiene los estados explorados
        self.frontier = PriorityQueue()  # Contiene los estados de frontera en orden de prioridad segun heuristica
        self.start = start  # Contiene el estado inicial
        self.goal = goal  # Contiene el estado al que se busca llegar
        self.ProblemState = problem_state

    def check_if_visited(self, new_state):
        pass

    def solve(self):
        start_state = self.ProblemState(self.start, 0, 0, self.start, self.goal)

        # Verificar si el problema ya viene resuelto
        if start_state.goal_test():
            print("El problema viene resuelto.")
            return start_state.path

        count = 0

        # Iniciar la priority queue en el estado inicial. Se le agrega la tupla (heuristica, contador, estado)
        self.frontier.put((0, count, start_state))

        # Ejecutar hasta que se tenga una solucion o hasta que se acaben los estados de frontera
        while not self.path and self.frontier.qsize():
            closest_child = self.frontier.get()[2]  # Obtiene el estado con mas prioridad
            closest_child.generate_frontier()
            self.visitedQueue.append(closest_child.state)  # Agregar el estado actual a los estados visitados.

            # Agregar los nuevos estados frontera al listado de frontera general
            for child in closest_child.frontier:
                if child.state not in self.visitedQueue:
                    count += 1
                    # Funcion goal_test
                    if child.goal_test():  # Sera true si es el estado final que se busca
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

    a = AStarSolver(StateString, start1, goal1)
    a.solve()
    for i in range(len(a.path)):
        print("%d) " % i + a.path[i])
