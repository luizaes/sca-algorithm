#include <bits/stdc++.h>
#include "benchmark.hpp"

using namespace std;

struct Agent {
	vector<double> solution;
};

class SCA {

public:
	SCA(int number, int iteration);
	~SCA();
	void initPopulation(Benchmark function);
	vector<Agent> getSolutions();
	int getIterations();
	int getAgents();
	int getDimensions();

private:
	int numberAgents;
	int maxIterations;
	int numberDimensions;
	vector<Agent> solutions;
};