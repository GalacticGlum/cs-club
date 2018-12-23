#include <string>

#include "Testcase.h"
#include "Random.h"
#include "IostreamHelper.h"
#include <ctime>

int main(int argc, int** argv)
{
	Random::Initialize();

	const int minimumNodes = IostreamHelper::ReadInput<int>("Min N: ");
	const int maximumNodes = IostreamHelper::ReadInput<int>("Max N: ");
	const int minimumRoutes = IostreamHelper::ReadInput<int>("Min M: ");
	const int maximumRoutes  = IostreamHelper::ReadInput<int>("Max M: ");
	const int minimumTotalCities = IostreamHelper::ReadInput<int>("Min K: ");
	const int maximumTotalCities = IostreamHelper::ReadInput<int>("Max K: ");

	const int testcases = IostreamHelper::ReadInput<int>("Test case amount: ");
	const std::string testcasePrefix = IostreamHelper::ReadInput<std::string>("Test case file prefix: ");

	std::vector<int> nodes = Random::UniformVector(minimumNodes, maximumNodes + 1, testcases);
	std::vector<int> routes = Random::UniformVector(minimumRoutes, maximumRoutes + 1, testcases);
	for(int i = 0; i < testcases; ++i)
	{
		const int n = nodes[i];
		const int m = routes[i];

		std::cout << "Started test case" << i+1 << " (n=" << n << ", m=" << m << ")" << std::endl;
		std::string filename = testcasePrefix + "." + std::to_string(i+1);
		Testcase testcase(n, m, minimumTotalCities, maximumTotalCities);

		const time_t startTime = time(nullptr);
		testcase.Generate(filename);
		const time_t endTime = time(nullptr);

		std::cout << "Completed test case " << i+1 << " in " << endTime-startTime << " sec." << std::endl;
	}
}
