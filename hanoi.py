from typing import List

class Disc: 
    def __init__(self, size):
        self.size = size

    def getSize(self):
        return self.size
    

class Tower:
    def __init__(self, initial_discs: int = None, name: str = "Tower"):
        self.discs: List[Disc] = [Disc(size=i) for i in range(initial_discs, 0, -1)]  # Create discs in descending order
        self.name = name

    def add(self, disc: Disc):
        if len(self.discs) == 0 or self.discs[-1].getSize() > disc.getSize():
            self.discs.append(disc)
    
    def pop(self): 
        if self.discs and len(self.discs) > 0:
            return self.discs.pop()

    def getName(self):
        return self.name

    def __repr__(self):
        return f"Tower {self.getName()}: [{', '.join(str(disc.getSize()) for disc in self.discs)}]"



class HanoiSolver: 
    def __init__ (self, no_discs: int):
        self.no_discs = no_discs
        self.towers: List[Tower] = [Tower(no_discs, "A"), Tower(0, "B"), Tower(0, "C")]
        print(f"Initial state\n{self.towers}")
        print("---------------------------------------------")


    def nextStep(self, src: int, dst: int, nr_discs: int):
        if nr_discs == 1:
            disc_to_replace = self.towers[src].pop()
            if disc_to_replace is not None:
                self.printLine(disc_to_replace, src, dst)
                print(self.towers)
                self.towers[dst].add(disc_to_replace)
            print("---------------------------------------------")

        else: 
            aux = 3 - src - dst # finding the index of the auxilary tower
            self.nextStep(src, aux, nr_discs - 1)
            self.towers[dst].add(self.towers[src].pop())
            self.nextStep(aux, dst, nr_discs - 1)
        
    def solve(self): 
        self.nextStep(0, 2, self.no_discs)

    def printLine(self, disc: Disc, src: int, dst: int):
        print(f"Move disc {disc.getSize()} from {self.towers[src].getName()} to {self.towers[dst].getName()}")

# test
class Main: 
    num = int (input("Enter number : "))
    obj = HanoiSolver(num)
    obj.solve()