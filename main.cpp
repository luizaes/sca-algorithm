#include "sca.hpp"

int main() {

	SCA sca = SCA(30, 500, 20);
	Benchmark func = Benchmark(1, -100, 100);
	int contador = 0;
	double evaluation = 0, best = 0;
	vector<Agent> solutions, bestSolution;

	// Initializes the initial population
	sca.initPopulation(func);

	//vector<Agent> solutions = sca.getSolutions();

	// for(int i = 0; i < sca.getAgents(); i++) {
	// 	for(int j = 0; j < sca.getDimensions(); j++) {
	// 		cout << solutions[i].solution[j] << " ";
	// 	}
	// 	cout << endl;
	// }

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

		// Update random numbers
		

		// Update the position of the agents

		contador++;
	} while(contador < sca.getIterations());

	return 0;
}