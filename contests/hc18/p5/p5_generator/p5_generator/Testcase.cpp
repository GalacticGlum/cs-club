#include "Testcase.h"
#include "Random.h"

#include <set>
#include <numeric>
#include <queue>
#include <fstream>
#include "Solver.h"
#include <igraph/igraph.h>

Testcase::Testcase(const int n, const int m, const int minimumTotalCities, const int maximumTotalCities) :
	m_NodeCount(n), m_RouteCount(m)
{
	igraph_t graph;

	igraph_tree(&graph, m_NodeCount, Random::Range(2, 100), IGRAPH_TREE_UNDIRECTED);

	igraph_eit_t edgeIterator;
	igraph_eit_create(&graph, igraph_ess_all(IGRAPH_EDGEORDER_ID), &edgeIterator);

	while(!IGRAPH_EIT_END(edgeIterator))
	{
		const igraph_integer_t edgeId = IGRAPH_EIT_GET(edgeIterator);
		igraph_integer_t u, v;
		igraph_edge(&graph, edgeId, &u, &v);

		m_Edges.emplace_back(u+1,v+1);
		IGRAPH_EIT_NEXT(edgeIterator);
	}

	for(long i = 0; i < m_RouteCount; ++i)
	{
		int v = Random::Range(1, m_NodeCount);
		int k = Random::Range(minimumTotalCities, maximumTotalCities);
		m_Routes.emplace_back(v, k);
	}

	igraph_destroy(&graph);
}

void Testcase::Generate(const std::string& filename)
{
	std::ofstream inputFile, outputFile;
	inputFile.open(filename + ".in");
	outputFile.open(filename + ".out");

	inputFile << m_NodeCount << " " << m_RouteCount << std::endl;
	for (auto& e : m_Edges)
	{
		inputFile << e.first << " " << e.second << std::endl;
	}

	for(auto& route : m_Routes)
	{
		inputFile << route.first << " " << route.second << std::endl;
	}

	Solver solver(m_NodeCount, m_Edges, m_Routes);
	for (auto& s : solver.Solve())
	{
		outputFile << s << std::endl;
	}

	inputFile.close();
	outputFile.close();
}