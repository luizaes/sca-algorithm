#include "sca.hpp"

int main() {

	SCA sca = SCA(30, 500);
	Benchmark func = Benchmark(1, -100, 100);

	sca.initPopulation(func);

	for(int i = 0; i < sca.getIterations(); i++) {

	}

	return 0;
}