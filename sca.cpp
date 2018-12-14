#include "sca.hpp"

SCA::SCA(int number, int iteration, int dimensions) {
	numberAgents = number;
	maxIterations = iteration;
	numberDimensions = dimensions;
}

SCA::~SCA() {
	
}

void SCA::initPopulation(Benchmark function) {
		
	unsigned seed = chrono::system_clock::now().time_since_epoch().count();
	mt19937 generator(seed);
	uniform_real_distribution<double> distribution(function.getLowerBound(),function.getUpperBound());
	double aux;

	for(int i = 0; i < numberAgents; i++) {
		solutions.push_back(Agent());
		for(int j = 0; j < numberDimensions; j++) {
			aux = distribution(generator);
			solutions[i].solution.push_back(aux);
		}
	}
}

vector<Agent> SCA::getSolutions() {
	return solutions;
}

int SCA::getIterations() {
	return maxIterations;
}

int SCA::getAgents() {
	return numberAgents;
}

int SCA::getDimensions() {
	return numberDimensions;
}