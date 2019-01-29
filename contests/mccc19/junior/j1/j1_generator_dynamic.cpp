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

#define MIN_FREQUENCY 20LL
#define MAX_FREQUENCY 20000LL
const float THIRD = 1/3.0f;

void GenerateTestcase(long long queries)
{
    std::cout << queries << "\n";
    for(long long i = 0; i < queries; ++i)
    {
        long long f1 = 0, f2 = 0;
        float chance = Random::Value();
        if(chance < THIRD) // f2 > f1
        {
            f1 = Random::Range(MIN_FREQUENCY, MAX_FREQUENCY - 1);
            f2 = Random::Range(f1+1, MAX_FREQUENCY);
        }
        else if(chance >= THIRD && chance < 2 * THIRD) // f2 < f1
        {
            f1 = Random::Range(MIN_FREQUENCY+1, MAX_FREQUENCY);
            f2 = Random::Range(MIN_FREQUENCY, f1 - 1);
        }
        else if(chance >= 2 * THIRD && chance <= 1) // f2=f1
        {
            f1 = f2 = Random::Range(MIN_FREQUENCY, MAX_FREQUENCY);
        }
        
        std::cout << f1 << " " << f2 << "\n";
        std::string solution = "none";
        if (f2 > f1)
        {
            solution = "towards";
        }
        else if(f2 < f1)
        {
            solution = "away";
        }

        std::cerr << solution << "\n";
    }
}

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

int main(int argc, char** argv) 
{
    Random::Initialize(0xdeadbeef);
    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    
    long long minQueries = stoll(params[0]), maxQueries = stoll(params[1]);
    long long queries = Random::Range(minQueries, maxQueries);
    GenerateTestcase(queries);
}