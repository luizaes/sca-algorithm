#include "sca.hpp"

SCA::SCA(int number, int iteration, int dimensions) {
	numberAgents = number;
	maxIterations = iteration;
	numberDimensions = dimensions;
	a = 2;

	generator.seed(std::chrono::high_resolution_clock::now().time_since_epoch().count());
}

SCA::~SCA() {
	
}

void SCA::initPopulation(Benchmark function) {
	
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

void SCA::update(Benchmark function, vector<double> best, int iteration) {

	double r1, r2, r3, r4;
	uniform_real_distribution<double> distribution(0.0,1.0);

	r1 = a - (iteration * (a/maxIterations));
	r2 = (2*M_PI) * distribution(generator);
    r3 = 2 * distribution(generator);
	r4 = distribution(generator);

	for(int i = 0; i < numberAgents; i++) {
		for(int j = 0; j < numberDimensions; j++) {
			if(r4 < 0.5) {
				// Xi+1 = Xi + r1 * sin(r2) * abs(r3 * Pi - Xi)
				solutions[i].solution[j] = solutions[i].solution[j] + r1 * sin(r2) * abs(r3 * best[j] - solutions[i].solution[j]);
			} else if(r4 >= 0.5) {
				solutions[i].solution[j] = solutions[i].solution[j] + r1 * cos(r2) * abs(r3 * best[j] - solutions[i].solution[j]);
			}
		}
	}
}