#  Universidad del Valle de Guatemala
#  Inteligencia Artificial
#  Eric Mendoza: 15002
#  Proyecto 1: Agente inteligente
#  AStar.py: El presente archivo ejecuta una version generica de A*

from queue import PriorityQueue


class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def get_dist(self):
        pass

    def create_children(self):
        pass


class StateString(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.dist = self.get_dist()

    def get_dist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def create_children(self):
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = StateString(val, self)
                self.children.append(child)


class AStarSolver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        start_state = StateString(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, start_state))
        while not self.path and self.priorityQueue.qsize():
            closest_child = self.priorityQueue.get()[2]
            closest_child.create_children()
            self.visitedQueue.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Problema no tiene solucion.")
        return self.path


if __name__ == "__main__":
    start1 = "cire"
    goal1 = "eric"
    print("Starting...")
    a = AStarSolver(start1, goal1)
    a.solve()
    for i in range(len(a.path)):
        print("%d) " % i + a.path[i])
