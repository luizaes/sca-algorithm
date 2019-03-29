import numpy as np
import random
import math

def funcObjective(individual, type):
	fitness = 0
	if type == 1:
		for x in range(0,len(individual)):
			fitness = fitness + individual[x] ** 2
	elif type == 2:
		for x in range(0,len(individual)-1):
			fitness = fitness + (100.0 * (individual[x+1]-individual[x]**2) ** 2) + (1.0-individual[x]) ** 2
	elif type == 3:
		for x in range(0,len(individual)):
			fitness = fitness + individual[x] ** 2 - 10 * math.cos(2*math.pi*individual[x]) + 10
	return fitness

maxIteration = 500
dim = 20
searchAgents = 30
func = 2
lowerBound = -5
upperBound = 10

bestSolution = []
best = 0
contador = 1

population = []

for x in range(0,searchAgents):
	individual = []
	for y in range(0,dim):
		individual.append(random.uniform(lowerBound, upperBound))
	population.append(individual)

#print(population)

for x in range(0,searchAgents):
	fitness = funcObjective(population[x], func)
	if x == 0:
		bestSolution = population[x]
		best = fitness
	elif fitness < best:
		best = fitness
		bestSolution = population[x]

while contador < maxIteration:
	a = 2
	r1 = a-contador*((a)/maxIteration)

	for x in range(0,searchAgents):
		for y in range(0,dim):
			r2 = 2*math.pi*random.uniform(0.0,1.0)
			r3 = 2*random.uniform(0.0,1.0)
			r4 = random.uniform(0.0,1.0)

			if r4 < 0.5:
				population[x][y] = population[x][y]+(r1*math.sin(r2)*abs(r3*bestSolution[y]-population[x][y]))
				if population[x][y] > upperBound or population[x][y] < lowerBound:
					population[x][y] = random.uniform(lowerBound,upperBound)
			else:
				population[x][y] = population[x][y]+(r1*math.cos(r2)*abs(r3*bestSolution[y]-population[x][y]))
				if population[x][y] > upperBound or population[x][y] < lowerBound:
					population[x][y] = random.uniform(lowerBound,upperBound)			

	for x in range(0,searchAgents):
		fitness = funcObjective(population[x], func)
		if fitness < best:
			best = fitness
			bestSolution = population[x]
	contador = contador + 1

print(bestSolution)
print(best)