#include "sca.hpp"

int main() {

	SCA sca = SCA(30, 500, 20);
	Benchmark func = Benchmark(2, -32, 32);
	int contador = 0;
	double evaluation = 0, best = 0;
	vector<Agent> solutions;
	vector<double> bestSolution;

	// Initializes the initial population
	sca.initPopulation(func);

	do {
		solutions = sca.getSolutions();
		// Evaluate the solutions and update the best solution so far
		for(int i = 0; i < sca.getAgents(); i++) {
			evaluation = func.objectiveFunction(solutions[i].solution);
			if(i == 0) {
				best = evaluation;
				bestSolution = solutions[i].solution;
			} else if(evaluation < best) {
				best = evaluation;
				bestSolution = solutions[i].solution;
			}
		}

		// Update random numbers and update the position of the agents
		sca.update(func, bestSolution, contador);

		contador++;
	} while(contador < sca.getIterations());

	solutions = sca.getSolutions();

	for(int i = 0; i < sca.getAgents(); i++) {
		evaluation = func.objectiveFunction(solutions[i].solution);
		if(i == 0) {
			best = evaluation;
			bestSolution = solutions[i].solution;
		} else if(evaluation < best) {
			best = evaluation;
			bestSolution = solutions[i].solution;
		}
	}

	cout << "Variables: " << endl;
	for(int i = 0; i < bestSolution.size(); i++) {
		cout << bestSolution[i] << " ";
	}
	cout << endl;

	cout << "Best: " << best << endl;

	return 0;
}