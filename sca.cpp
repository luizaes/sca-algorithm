#include "sca.hpp"

SCA::SCA(int number, int iteration) {
	numberAgents = number;
	maxIterations = iteration;
}

SCA::~SCA() {
	
}

void SCA::initPopulation(Benchmark function) {
		
	unsigned seed = chrono::system_clock::now().time_since_epoch().count();
	mt19937 generator(seed);
	uniform_real_distribution<double> distribution(function.getLowerBound(),function.getUpperBound());

	for(int i = 0; i < numberAgents; i++) {
		for(int j = 0; j < numberDimensions; j++) {
			solutions[i].solution[j] = distribution(generator);
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