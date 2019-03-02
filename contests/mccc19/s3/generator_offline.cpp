#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>
#include <fstream>

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

const int MOD = 131071;
const int MAXN = 1e6+5;
typedef long long ll;

int dp[MAXN], all[MAXN], preall[MAXN];

#define MIN_GEN_N 1
#define MAX_GEN_N 1000000
#define TESTCASES 10
const std::string TESTCASE_PREFIX = "s3.3";

int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

    Random::Initialize();
    
    for(int i = 0; i < TESTCASES; ++i)
    {
        std::ofstream inputFile;
        inputFile.open(TESTCASE_PREFIX + "." + std::to_string(i+1) + ".in");

        int n = Random::Range(MIN_GEN_N, MAX_GEN_N);
        inputFile << n << "\n";

        std::vector<int> grades = Random::Vector(0, 100, n);
        std::vector<int> values = Random::Vector(1, 1000000000, n);

        for(int& value : values)
        {
            inputFile << value << " ";
        }
        
        inputFile << "\n";

        for(int& grade : grades) 
        {
            inputFile << grade << " ";
        }

        inputFile << "\n";
        inputFile.close();

        std::ofstream outputFile;
        outputFile.open(TESTCASE_PREFIX + "." + std::to_string(i+1) + ".out");

        all[0] = preall[0] = 1;
        for(int i = 1; i <= n; ++i)
        {
            if(i == 1)
            {
                all[i] = 1;
            }
            else
            {
                all[i] = all[i - 1] * 2LL % MOD;
            }
            
            preall[i] = (preall[i - 1] + all[i]) % MOD;
        }

        ll mul = 0, add = 0;
        for(int i = 1; i <= n; ++i)
        {
            mul = (mul + preall[i - 1]) % MOD;
            dp[i] = (2LL * dp[i - 1] + (ll)add + mul * (ll)values[i-1] % MOD) % MOD;
            add = (add + (ll)values[i-1] * preall[i - 1] % MOD) % MOD;
        }

        float weight = (float)dp[n]/MOD;
        for(int& grade : grades)
        {
            float finalGrade = std::round(grade * weight * 100) / 100;
            outputFile << finalGrade << " ";
        }

        outputFile << "\n";
        outputFile.close();
    }
}