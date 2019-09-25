#pragma once
#include <vector>
#include <strstream>

class Testcase
{
public:
	Testcase(int n, int m, int minimumTotalCities, int maximumTotalCities);

	void Generate(const std::string& filename);
private:
	int m_NodeCount;
	int m_RouteCount;

	std::vector<std::pair<int, int>> m_Edges;
	std::vector<std::pair<int, int>> m_Routes;
};

