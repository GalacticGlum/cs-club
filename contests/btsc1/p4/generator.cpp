#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>
#include <unordered_map>

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

    static std::string String(std::size_t length )
    {
        auto charset = []() -> char
        {
            const char charset[] =
            "0123456789"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz";

            const std::size_t maxIndex = (sizeof(charset) - 1);
            return charset[Range(static_cast<std::size_t>(0), maxIndex - 1)];
        };

        std::string result(length, 0);
        std::generate_n(result.begin(), length, charset);

        return result;
    }
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

int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

    Random::Initialize();

    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    int testcase = std::stoi(params[0]);
    Random::Initialize(testcase);

    std::string root = Random::String(Random::Range(1,100));
    std::string candidate = "";
    bool result = Random::Value() <= 0.5;
    // 50% chance that the string is valid
    if (result)
    {
        int n = Random::Range(1, 20000);
        while (candidate.size() < n)
        {
            candidate += root;
        }

        // Choose random points and insert the root string
        for (int i = 0; i < n; ++i)
        {
            // 5% chance
            if (Random::Value() > 0.05) continue;
            for (int j = 0; j < Random::Range(0, 10); ++j)
            {
                candidate = candidate.substr(0, j + 1) + root + candidate.substr(j + 1);
            }
        }
    }
    else
    {
        candidate = Random::String(Random::Range(1, 50000));
    }

    std::cout << root << "\n";
    std::cout << candidate << "\n";
    std::cerr << (result?"true":"false")<<"\n";
}