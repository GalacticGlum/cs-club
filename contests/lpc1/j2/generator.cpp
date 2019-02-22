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

int main(int argc, char** argv) 
{
    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    
    long long seed = stoll(params[0]);
    int minN = stoll(params[1]), maxN = stoll(params[2]);
    Random::Initialize(seed);
    
    int n = Random::Range(minN, maxN);
    std::cout << n << "\n";

    std::string password = Random::String(n);
    std::cout << password << "\n";

    std::map <char, int> m;

   for(auto c: numbers)
      m[c] = 0;
   for(auto c: lower_case)
      m[c] = 1;
   for(auto c: upper_case)
      m[c] = 2;
   for(auto c: special)
      m[c] = 3;
   
   std::set <int> types;

   for(auto c: password) {
      types.insert(m[c]);
   }

   std::cerr << std::max(6 - n, 4 - (int)types.size()) << "\n";
}