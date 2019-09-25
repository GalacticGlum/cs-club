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

const float QUARTER = 1/4.0f;

void GenerateTestcase(long long n)
{
    std::cout << n << "\n";
    for(long long i = 0; i < n; ++i)
    {
        std::string operationCode;
        int x = Random::Range(-10000, 10000);
        int y = Random::Range(-10000, 10000);

        float chance = Random::Value();
        float solution = 0;
        if(chance < QUARTER) 
        {
            operationCode = "ADD";
            solution = static_cast<float>(x)+y;
        }
        else if(chance >= QUARTER && chance < 2 * QUARTER)
        {
            operationCode = "SUB";
            solution = static_cast<float>(x)-y;
        }
        else if(chance >= 2 * QUARTER && chance < 3 * QUARTER)
        {
            operationCode = "MUL";
            solution = static_cast<float>(x)*y;
        }
        else if(chance >= 3 * QUARTER && chance <= 1)
        {
            operationCode = "DIV";
            if (y == 0)
            {
                y = 1;
            }
            
            solution = static_cast<float>(x)/y;
        }

        std::cout << operationCode << " " << x << " " << y << "\n";
        std::cerr << std::setprecision(2) << std::fixed;
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
    
    long long minN = stoll(params[0]), maxN = stoll(params[1]);
    long long n = Random::Range(minN, maxN);
    GenerateTestcase(n);
}