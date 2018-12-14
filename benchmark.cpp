#include "benchmark.hpp"

Benchmark::Benchmark(int number, double lower, double upper) {
	function = number;
	lowerBound = lower;
	upperBound = upper;
}

Benchmark::~Benchmark() {

}

double Benchmark::objectiveFunction(vector<double> solutions) {
	/* Defining fitness function - Sphere's function
	   Dimensions: d
	   Domain: x ∈ [-5.12, 5.12]
	   Global minimum: (0, ..., 0)
	*/
	if(function == 1) {
		double result = 0;
		for(int i = 0; i < solutions.size(); i++) {
			result += pow(solutions[i], 2);
		}
		return result;

	} else if(function == 2) {
		/* Defining fitness function - Ackley's function 
	       Dimensions: d
	       Domain: x ∈ [-32, 32]
	       Global minimum: (0, ..., 0)
		*/
		double aux = 0, aux1 = 0;

		for (int i = 0; i < solutions.size(); i++) {
        	aux += solutions[i]*solutions[i];
        }

        for (int i = 0; i < solutions.size(); i++) {
        	aux1 += cos(2.0*M_PI*solutions[i]);
        }

        return (-20.0*(exp(-0.2*sqrt(1.0/(double)solutions.size()*aux)))-exp(1.0/(double)solutions.size()*aux1)+20.0+exp(1));
	} else if(function == 3) {
		/* Defining fitness function - Rosenbrock's function 
		   Dimensions: d
		   Domain: x ∈ [-5, 10]
		   Global minimum: (1, ..., 1)
		*/
		double result = 0.0;

		for(int i = 0; i < solutions.size()-1; i++) {
        	result += 100.0 * pow((solutions[i+1] - pow(solutions[i],2.0)),2) + pow((1.0 - solutions[i]),2);
    	}

    	return result;
	} else if(function == 4) {
		/* Defining fitness function - Rastrigin's function 
		   Dimensions: d
		   Domain: x ∈ [-5.12, 5.12]
		   Global minimum: (0, ..., 0)
		*/
		double result = 0;

		for(int i = 0; i < solutions.size(); i++) {
	        result += pow(solutions[i], 2.0) - 10 * cos(2 * M_PI * solutions[i]) + 10;
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