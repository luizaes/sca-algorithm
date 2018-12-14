#include "benchmark.hpp"

Benchmark::Benchmark(int number, double lower, double upper) {
	function = number;
	lowerBound = lower;
	upperBound = upper;
}

Benchmark::~Benchmark() {

}

double Benchmark::objectiveFunction(vector<double> solutions) {
	// Sphere function
	if(function == 1) {
		double result = 0;
		for(int i = 0; i < solutions.size(); i++) {
			result += pow(solutions[i], 2);
		}
		return result;
	}
	return -1;
}

double Benchmark::getLowerBound() {
	return lowerBound;
}

double Benchmark::getUpperBound() {
	return upperBound;
}