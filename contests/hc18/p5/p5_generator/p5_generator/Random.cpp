#include "Random.h"

std::mt19937 Random::m_RandomEngine;

std::vector<int> Random::UniformVector(const int a, const int b, const int n)
{
	double x = a;
	std::vector<int> result;

	for (int i = n; i >= 0; --i)
	{
		x += (b - x) * (1 - std::pow(Value(), 1.0 / i));
		result.push_back(static_cast<int>(std::floor(x)));
	}

	return result;
}