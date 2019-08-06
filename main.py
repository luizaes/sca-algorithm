import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Funcao de mapeamento
def remap(number, fromMin, fromMax, toMin, toMax):

	fromAbs = number - fromMin
	fromMaxAbs = fromMax - fromMin

	normal = fromAbs / fromMaxAbs

	toMaxAbs = toMax - toMin
	toAbs = toMaxAbs * normal

	to = toAbs + toMin

	return to

# Funcao para calculo da diversidade
def diversityCalc(population, dim):
	ciVec = []
	for x in range(0,dim):
		ci = 0
		for y in range(0,len(population)):
			ci += population[y][x] / float(len(population))
		ciVec.append(ci)

	Isd = 0
	t1 = 0
	t2 = 0
	for x in range(0,dim):
		t1 = 0
		for y in range(0,len(population)):
			t2 = population[y][x] - ciVec[x]
			t1 += t2 * t2
		Isd += math.sqrt(t1/(len(population)-1))
	Isd /= float(dim)
	return Isd

# Mapas caoticos
def logisticMap(randomNum):
	randomNum = 4.0 * randomNum * (1 - randomNum)
	return randomNum

# Funcoes objetivo
def funcObjective(individual, type):
	fitness = 0
	top1 = 0
	top = 0

	if type == 1:
		# Esfera -5.12 .. 5.12
		for x in range(0,len(individual)):
			fitness = fitness + individual[x] ** 2
	elif type == 2:
		# Rosenbrock -30 .. 30
		for x in range(0,len(individual)-1):
			fitness = fitness + (100.0 * (individual[x+1]-individual[x]**2) ** 2) + (individual[x]-1.0) ** 2
	elif type == 3:
		# Rastrigin -5.12 .. 5.12
		for x in range(0,len(individual)):
			fitness = fitness + individual[x] ** 2 - 10 * math.cos(2*math.pi*individual[x]) + 10
	elif type == 4:
		# Schaffer -100 .. 100
		for x in range(0,len(individual)):
			top = top + (individual[x]**2)
		top = top ** 0.25
		for x in range(0,len(individual)):
			top1 = top1 + (individual[x] ** 2)
		top1 = top1 ** 0.1
		top1 = (math.sin(50*top1)**2) +1.0
		fitness = top * top1
	elif type == 5:
		# Ackley -32 .. 32
		aux = aux1 = 0.0
		for x in range(0, len(individual)):
			aux = aux + (individual[x]*individual[x])

		for x in range(0, len(individual)):
			aux1 = aux1 + math.cos(2.0*math.pi*individual[x])

		fitness = -20.0*(math.exp(-0.2*math.sqrt(1.0/len(individual)*aux)))-math.exp(1.0/len(individual)*aux1)+20.0+math.exp(1)
	elif type == 6:
		# Griewank -600 .. 600
		top1 = 0
		top2 = 1
		for x in range(0, len(individual)):
			top1 = top1 + individual[x] ** 2
			top2 = top2 * math.cos((((individual[x])/math.sqrt((x+1)))*math.pi)/180)
		fitness = (1/4000.0) * top1 - top2 + 1
	elif type == 7:
		# Schwefel -500 .. 500
		aux = 0.0
		for x in range(0, len(individual)):
			aux = aux + individual[x] * math.sin(math.sqrt(math.fabs(individual[x]))) 
		fitness = (-1*aux/len(individual))
	elif type == 8:
		# Zakharov -5 .. 10
		aux = aux1 = 0
		for x in range(0, len(individual)):
			aux = aux + individual[x] ** 2
			aux1 = aux1 + 0.5 * x * individual[x]
		
		fitness = aux + aux1 ** 2 + aux1 ** 4
	return fitness

# Parametros
maxIteration = 1000
dim = 20
searchAgents = 30
func = 8
lowerBound = -5
upperBound = 10
dist = 3
runs = 10

average = 0
averageNormalized = 0
finalSolutions = []
bestSolutionFinal = []
worstSolutionFinal = []
meanSolutionFinal = []
diversityFinal = []
lastBest = 0
std = 0

for z in range(0,runs):
	bestSolution = []
	bestFitness = []
	best = 0
	contador = 1
	population = []
	initialPoint = random.uniform(0.0,1.0)
	worst = 0
	mean = 0
	diversity = 0
	desvio = 1

	# Geracao da Populacao Inicial
	for x in range(0,searchAgents):
		individual = []
		for y in range(0,dim):
			# Uniforme
			if dist == 1:
				individual.append(random.uniform(lowerBound, upperBound))	
			# Logistico
			elif dist == 2:
				initialPoint = logisticMap(initialPoint)
				individual.append(remap(initialPoint, 0, 1, lowerBound, upperBound))
			# Gaussiana
			elif dist == 3:
				num = np.random.normal((lowerBound+upperBound)/2, upperBound-((lowerBound+upperBound)/2))
				if num < lowerBound:
					num = lowerBound
				if num > upperBound:
					num = upperBound
				individual.append(num)
		population.append(individual)

	#print(population)

	mean = 0
	# Avaliacao da Populacao Inicial
	for x in range(0,searchAgents):
		fitness = funcObjective(population[x], func)
		mean = mean + fitness
		if x == 0:
			bestSolution = population[x]
			best = fitness
			worst = fitness
		elif fitness < best:
			best = fitness
			bestSolution = population[x]
		elif worst < fitness:
			worst = fitness

	mean = mean / searchAgents

	diversity = diversityCalc(population, dim)

	if z == 0:
		bestSolutionFinal.append(best)
		worstSolutionFinal.append(worst)
		meanSolutionFinal.append(mean)
		diversityFinal.append(diversity)
	else:
		bestSolutionFinal[0] = bestSolutionFinal[0] + best 
		worstSolutionFinal[0] = worstSolutionFinal[0] + worst 
		meanSolutionFinal[0] = meanSolutionFinal[0] + mean
		diversityFinal[0] = diversityFinal[0] + diversity

	# Algoritmo Principal
	while contador < maxIteration:
		a = 2
		mean = 0
		r1 = a-contador*((a)/maxIteration)

		# Para cada agente de busca e para cada dimensao, faz o update
		for x in range(0,searchAgents):
				for y in range(0,dim):
					# Uniforme
					if dist == 1:
						r2 = 2*math.pi*random.uniform(0.0,1.0)
						r3 = 2*random.uniform(0.0,1.0)	
						r4 = random.uniform(0.0,1.0)	
					# Logistico
					elif dist == 2:
						initialPoint = logisticMap(initialPoint)
						r2 = 2*math.pi*initialPoint
						initialPoint = logisticMap(initialPoint)
						r3 = 2*initialPoint
						initialPoint = logisticMap(initialPoint)
						r4 = initialPoint
					# Gaussiana
					elif dist == 3:
						r2 = np.random.normal(0.5, 0.5)
						if r2 < 0:
							r2 = 0.0
						if r2 > 1:
							r2 = 1.0
						r2 = 2*math.pi*r2
						r3 = np.random.normal(0.5, 0.5)
						if r3 < 0:
							r3 = 0.0
						if r3 > 1:
							r3 = 1.0
						r3 = 2*r3
						r4 = np.random.normal(0.5, 0.5)
						if r4 < 0:
							r4 = 0.0
						if r4 > 1:
							r4 = 1.0

				
					if r4 < 0.5:
						population[x][y] = population[x][y]+(r1*math.sin(r2)*abs(r3*bestSolution[y]-population[x][y]))
						if population[x][y] > upperBound or population[x][y] < lowerBound:
							# Uniforme
							if dist == 1:
								population[x][y] = random.uniform(lowerBound, upperBound)
							# Logistico
							elif dist == 2:
								initialPoint = logisticMap(initialPoint)
								population[x][y] = remap(initialPoint, 0, 1, lowerBound, upperBound)
							# Gaussiana
							elif dist == 3:
								num = np.random.normal((lowerBound+upperBound)/2, upperBound-((lowerBound+upperBound)/2))
								if num < lowerBound:
									num = lowerBound
								if num > upperBound:
									num = upperBound
								population[x][y] = num
					else:
						population[x][y] = population[x][y]+(r1*math.cos(r2)*abs(r3*bestSolution[y]-population[x][y]))
						if population[x][y] > upperBound or population[x][y] < lowerBound:
							# Uniforme
							if dist == 1:
								population[x][y] = random.uniform(lowerBound, upperBound)
							# Logistico
							elif dist == 2:
								initialPoint = logisticMap(initialPoint)
								population[x][y] = remap(initialPoint, 0, 1, lowerBound, upperBound)
							# Gaussiana
							elif dist == 3:
								num = np.random.normal((lowerBound+upperBound)/2, upperBound-((lowerBound+upperBound)/2))
								if num < lowerBound:
									num = lowerBound
								if num > upperBound:
									num = upperBound
								population[x][y] = num
		
		mean = 0
		# Avalia novamente as solucoes
		for x in range(0,searchAgents):
			fitness = funcObjective(population[x], func)
			mean = mean + fitness
			if x == 0:
				worst = fitness
			if fitness < best:
				best = fitness
				bestSolution = population[x]
			elif worst < fitness:
				worst = fitness

		mean = mean / searchAgents

		diversity = diversityCalc(population, dim)

		if z == 0:
			bestSolutionFinal.append(best)
			worstSolutionFinal.append(worst)
			meanSolutionFinal.append(mean)
			diversityFinal.append(diversity)
		else:
			bestSolutionFinal[contador] = bestSolutionFinal[contador] + best
			worstSolutionFinal[contador] = worstSolutionFinal[contador] + worst
			meanSolutionFinal[contador] = meanSolutionFinal[contador] + mean
			diversityFinal[contador] = diversityFinal[contador] + diversity

		contador = contador + 1
		bestFitness.append(best)

	print("Melhor fitness da execucao:")
	print(best)
	finalSolutions.append(best)
	average = average + best

average = average/runs

for x in range(0,len(finalSolutions)):
	std = std + (finalSolutions[x] - average) ** 2

for x in range(0,len(bestSolutionFinal)):
	bestSolutionFinal[x] = bestSolutionFinal[x] / runs
	worstSolutionFinal[x] = worstSolutionFinal[x] / runs
	meanSolutionFinal[x] = meanSolutionFinal[x] / runs
	diversityFinal[x] = diversityFinal[x] / runs

print("-------------------- Informacoes das execucoes ------------------------")
print("Average: " + str(average))
std = math.sqrt(std/len(finalSolutions))
print("Std: " + str(std))

#plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
# axes.set_xlim([0, maxIteration])
# axes.set_ylim([0,100])

plt.plot([i for i in reversed(range(999))],[float(bestSolutionFinal[i]) for i in reversed(range(999))])
plt.plot([i for i in reversed(range(999))],[float(worstSolutionFinal[i]) for i in reversed(range(999))])
plt.plot([i for i in reversed(range(999))],[float(meanSolutionFinal[i]) for i in reversed(range(999))])
plt.ylabel('Fitness')
plt.xlabel('Iterations')
plt.title('Convergence Graph')
plt.show()

plt.plot([i for i in reversed(range(999))],[(round(diversityFinal[i], 2)) for i in reversed(range(999))])
plt.ylabel('Diversity')
plt.xlabel('Iterations')
plt.title('Diversity Graph')
plt.show()
