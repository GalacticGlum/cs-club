#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>

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

typedef unsigned long long ull;

int factorial(int n)
{
    if (n == 0 || n == 1) return 1;

    return n * factorial(n - 1);
}

int choose(int n, int k)
{
    int lower = factorial(k);

    int total = 1;
    for (int i = n; i > n - k; --i)
    {
        total *= i;
    }

    return total / lower;
}

int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    
    ull max = stoll(params[0]);
	int n = static_cast<int>(Random::Range(3ULL, max));
	int b = Random::Range(2, 25);
	int a = Random::Range(1, b - 1);
	std::cout << n << "\n";
	std::cout << a << " " << b << "\n";

	int range = b - a - 1;
	if (n - 2 == range)
    {
        std::cerr << 1 << "\n";
    }
    else if (range < n - 2)
    {
        std::cerr << 0 << "\n";
    }
    else
    {
        std::cerr << choose(range, n - 2) << "\n";
    }
}