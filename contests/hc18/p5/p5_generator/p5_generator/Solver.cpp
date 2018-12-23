#include "Solver.h"
#include <algorithm>
#include <utility>

Solver::Solver(const int n, std::vector<std::pair<int, int>> edges, std::vector<std::pair<int, int>> routes) : m_NodeCount(n), m_Routes(std::move(routes))
{
	m_Adjacency = std::vector<std::vector<int>>(m_NodeCount+1);
	m_PrimaryCache = std::vector<int>(m_NodeCount+1, 0);
	m_SecondaryCache = std::vector<int>(m_NodeCount+1, 0);
	m_DistanceCache = std::vector<int>(m_NodeCount+1, 0);

	for(auto& edge : edges)
	{
		m_Adjacency[edge.first-1].push_back(edge.second-1);
		m_Adjacency[edge.second-1].push_back(edge.first-1);
	}
}

void Solver::DFS(const int u, const int p)
{
	for(auto& v : m_Adjacency[u])
	{
		if (v == p) continue;
		DFS(v, u);
		if(m_PrimaryCache[v]+1 > m_SecondaryCache[u])
		{
			m_SecondaryCache[u] = m_PrimaryCache[v] + 1;
			if(m_SecondaryCache[u] > m_PrimaryCache[u])
			{
				std::swap(m_SecondaryCache[u], m_PrimaryCache[u]);
			}
		}
	}
}

void Solver::CacheDFS(const int u, const int p, const int k)
{
	m_DistanceCache[u] = std::max(m_PrimaryCache[u], k);
	for(auto& v : m_Adjacency[u])
	{
		if (v == p) continue;
		CacheDFS(v, u, std::max(m_PrimaryCache[v] + 1 == m_PrimaryCache[u] ? m_SecondaryCache[u] : m_PrimaryCache[u], k) + 1);
	}
}

std::vector<long long> Solver::Solve()
{
	std::vector<long long> result;

	DFS(0, -1);
	CacheDFS(0, -1, 0);
	const long long diameter = *std::max_element(m_DistanceCache.begin(), m_DistanceCache.end());
	for(auto& route : m_Routes)
	{
		const int x = route.first-1;
		const int y = route.second;
		result.push_back((y - 1)*diameter + m_DistanceCache[x]);
	}

	return result;
}
