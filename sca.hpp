#include <bits/stdc++.h>
#include "benchmark.hpp"

using namespace std;

struct Agent {
	vector<double> solution;
};

class SCA {

public:
	SCA(int number, int iteration, int dimensions);
	~SCA();
	void initPopulation(Benchmark function);
	vector<Agent> getSolutions();
	int getIterations();
	int getAgents();
	int getDimensions();
	void update(Benchmark function, vector<double> best, int iteration);

private:
	int numberAgents;
	int maxIterations;
	int numberDimensions;
	vector<Agent> solutions;
	mt19937 generator;
	int a;
};