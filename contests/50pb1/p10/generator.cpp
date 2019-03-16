#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>
#include <iomanip>

class Random
{
public:
	static void Initialize() { Initialize(static_cast<unsigned int>(time(NULL))); }
	static void Initialize(const unsigned int seed) { m_RandomEngine = std::mt19937(seed); }

	template <bool is_integral, typename T> struct uniform_distribution_selector;
	template <typename T> struct uniform_distribution_selector<true, T>
	{
		using type = std::uniform_int_distribution<T>;
	};
	template <typename T> struct uniform_distribution_selector<false, T>
	{
		using type = std::uniform_real_distribution<T>;
	};

	template<typename T>
	static T Range(T min, T max)
	{
		using uniform_distribution_type = typename uniform_distribution_selector<std::is_integral<T>::value, T>::type;
		return (uniform_distribution_type(min, max))(m_RandomEngine);
	}

    template<typename T>
	static std::vector<T> UniformVector(T a, T b, T n)
    {
        double x = a;
        std::vector<T> result;

        for (T i = n; i >= 0; --i)
        {
            x += (b - x) * (1 - std::pow(Value(), 1.0 / i));
            result.push_back(static_cast<T>(std::floor(x)));
        }

        return result;
    }

	template <typename T>
	static T Choose(T begin, T end)
	{
		unsigned long long k = Range(0, std::distance(begin, end)-1);
		std::advance(begin, k);
		return begin;
	}

	template <typename T>
	static std::vector<T> Vector(T min, T max, int n)
	{
		std::vector<T> result;
		for (int i = 0; i < n; ++i)
		{
			result.push_back(Range(min, max));
		}

		return result;
	}

	static float Value() { return Range<float>(0.0f, 1.0f); }
private:
	static std::mt19937 m_RandomEngine;
};

std::mt19937 Random::m_RandomEngine;

std::vector<std::string> split(const std::string& value, const std::string delimiter)
{
  std::string s(value);
  std::vector<std::string> result;
  
  size_t pos = 0;
  std::string token;
  while ((pos = s.find(delimiter)) != std::string::npos)
  {
      token = s.substr(0, pos);
      result.push_back(token);
      s.erase(0, pos + delimiter.length());
  }
  
  result.push_back(s);
  return result;
}

#define MAXN 1001
int distances[MAXN][MAXN];
int weights[MAXN][MAXN];

int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

	Random::Initialize();
	
	for(int i = 0; i < MAXN; ++i)
	{
	    for(int j = 0; j < MAXN; ++j)
	    {
	        distances[i][j] = weights[i][j] = 0;
	    }
	}
	
	int n = Random::Range(2, 1000);
	int m = Random::Range(1, 1000);
	std::cout << n << " " << m << "\n";
	for(int i = 1; i <= n; ++i)
	{
		for(int j = 1; j <= n; ++j)
		{
			weights[i][j] = i == j ? 0 : Random::Range(1, 100);
			std::cout << weights[i][j] << " ";
		}

		std::cout << "\n";
	}

	for(int i = 1; i <= n; ++i)
	{
		for(int j = i + 1; j <= n; ++j)
		{
			distances[i][j] = distances[j][i] = Random::Range(1, 100);
			std::cout << i << " " << j << " " << distances[i][j] << "\n"; 
		}
	}

	std::vector<int> traveled(m);
	int total_fare = 0;
	for(int i = 0; i < m; ++i)
	{
		traveled[i] = Random::Range(1, n);
		if (traveled[i] == traveled[i - 1])
		{
		    if(traveled[i] == n)
		    {
		        traveled[i] -= 1;
		    }
		    else
		    {
		        traveled[i] += 1;
		    }
		}
		
		std::cout << traveled[i] << " "; 
	}

	std::cout << "\n";
	
	for(int i = 0; i < m - 1; ++i)
	{
	    total_fare += distances[traveled[i]][traveled[i + 1]] * weights[traveled[i]][traveled[i + 1]];
	}
	
	std::cerr << total_fare << "\n";
}