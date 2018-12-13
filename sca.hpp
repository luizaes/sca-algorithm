class SCA {

public:
	SCA(int number, int iteration);
	~SCA();
	void init();
	void initPopulation();
	int numberAgents;
	int maxIterations;
};