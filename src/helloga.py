#!/usr/bin/python3

__author__ = "elek"
__date__ = "$Dec 16, 2010 5:36:12 PM$"

import random

def selection(population, fitnesse):
    def select_one(population):
        mno = len(population)-1
        s1 = population[random.randint(0, mno)]
        s2 = population[random.randint(0, mno)]
        if fitnesse(s1) > fitnesse(s2):
            return s2
        else:
            return s1
    return select_one(population), select_one(population)
   

def crossover(c1, c2):
    if (random.randint(0, 10) < 3):
        sep = random.randint(0, len(c1) - 1)
        return c1[:sep] + c2[sep:], c2[:sep] + c1[sep:]
    else:
        return (c1,c2)

def mutation(c1):
    if (random.randint(0, 10) < 5):
        sep = random.randint(0, len(c1) - 1)
        off = random.randint(-5, 5)
        return c1[:sep] + chr(ord(c1[sep]) + off) + c1[sep + 1:]
    else:
        return c1

def fitnesse(ch, target):
    if len(target) != len(ch):
        return None
    else:
        f = 0
        for i in range(len(target)):
            f += abs(ord(target[i]) - ord(ch[i]))
        return f


def initPopulation(num, ln):
    pop = []
    for i in range(num):
        pop.append("".join([chr(i) for i in random.sample(range(97, 122), 10)]))
    return pop



class GA:

    def __init__(self,target,initPopulationFunction,fitnesseFunction,selectionFunction,crossoverFunction,mutationFunction,):
        self.target = target
        self.initPopulation = initPopulationFunction
        self.fitnesse = fitnesseFunction
        self.mutation = mutationFunction
        self.crossover = crossoverFunction
        self.selection = selectionFunction

    def findBest(self,population, fitnes):
        f = -1
        r = None
        for x in population:
            if f == -1 or fitnes(x) < f:
                r = x
                f = fitnes(x)
        return r

    def live(self):
        currentGen = self.initPopulation(30, 11)
        f = lambda x: self.fitnesse(x, self.target)
        for i in range(150):
            nextGen = []
            while len(nextGen) < len(currentGen):
                p1, p2 = self.selection(currentGen, f)
                c1, c2 = self.crossover(p1, p2)
                nextGen.append(mutation(c1))
                nextGen.append(mutation(c2))
            currentGen = nextGen
            best = self.findBest(currentGen, f)
            b = f(best)
            print("{2}. generation --  best: {0} ({1})".format(best, b, i))


if __name__ == '__main__':
    ga = GA("helloworld",initPopulation,fitnesse,selection,crossover,mutation)
    ga.live()


