#include <bits/stdc++.h>

using namespace std;

class Benchmark {

public:
	Benchmark(int number, double lower, double upper);
	~Benchmark();
	double objectiveFunction(vector<double> solutions);
	double getLowerBound();
	double getUpperBound();
	
private:
	int function;
	double lowerBound;
	double upperBound;
};