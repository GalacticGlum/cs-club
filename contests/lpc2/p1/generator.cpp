#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>

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
	
	static std::string String(const size_t length)
    {
        std::string result;
        for(int i = 0; i < length; ++i)
        {
            result += 'a' + (Random::Range(0, 100) % 26);
        }
        
        return result;
    }

	static float Value() { return Range<float>(0.0f, 1.0f); }
private:
	static std::mt19937 m_RandomEngine;
};

std::mt19937 Random::m_RandomEngine;

const float QUARTER = 1/4.0f;

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

const int N = 200005;

const std::string numbers = "0123456789";
const std::string lower_case = "abcdefghijklmnopqrstuvwxyz";
const std::string upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const std::string special = "!@#$%^&*()-+";

struct Triplet
{
    int a, b, c;
    int sum() { return a + b + c; }
    bool invalid() { return a == 0 || b == 0 || c == 0; }
};

Triplet FindBiggestTriple(int perimeter)
{
    std::vector<Triplet> triples;
    int maxSideLength = perimeter / 2;

    for (int a = 1; a <= maxSideLength; ++a)
    {
        for (int b = 1; b <= a; ++b)
        {
            for (int c = 1; c <= b; ++c)
            {
                if (c * c + b * b == a * a)
                {
                    if (c + b + a < perimeter)
                    {
                        triples.push_back({c,b,a});
                    }
                }
            }
        }
    }

    // found nothing
    if (triples.size() == 0) return {-1,-1,-1};
    Triplet largestTriple = {0, 0, 0};
    for (Triplet triple : triples)
    {
        if (largestTriple.sum() < triple.sum())
        {
            largestTriple = triple;
        }
    }

    return largestTriple;
}

int main(int argc, char** argv) 
{
    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    
    long long seed = stoll(params[0]);
    Random::Initialize(seed);
    
    int n = Random::Range(1, 10);
    std::cout << n << "\n";
    for (int i = 0; i < n; ++i)
    {
        std::vector<int> values = Random::Vector(1, 100, 3);
        std::sort(values.begin(), values.end());
        int a = values[0];
        int b = values[1];
        int c = values[2];
        std::cout << a << " " << b << " " << c << "\n";

        if (a * a + b * b == c * c)
        {
            std::cerr << "true\n";
        }
        else
        {
            Triplet triple = FindBiggestTriple(a + b + c);
            if (triple.invalid())
            {
                std::cerr << "false\n";
            }
            else
            {
                std::cerr << triple.a << " " << triple.b << " " << triple.c << "\n";
            }
        }
    }
}