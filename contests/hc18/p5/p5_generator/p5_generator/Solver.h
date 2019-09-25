#pragma once
#include <vector>

class Solver
{
public:
	Solver(int n, std::vector<std::pair<int, int>> edges, std::vector<std::pair<int, int>> routes);

	std::vector<long long> Solve();
private:
	int m_NodeCount;

	std::vector<std::vector<int>> m_Adjacency;
	std::vector<int> m_PrimaryCache;
	std::vector<int> m_SecondaryCache;
	std::vector<int> m_DistanceCache;
	std::vector<std::pair<int, int>> m_Routes;

	void DFS(int u, int p);
	void CacheDFS(int u, int p, int k);
};

