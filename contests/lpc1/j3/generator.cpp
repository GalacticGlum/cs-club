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

int a[102][102];

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int main(int argc, char** argv) 
{
    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    
    long long seed = stoll(params[0]);
    Random::Initialize(seed);
    
    long long h = Random::Range(1, 100);
    long long w = Random::Range(1, 100);
    std::cout << h << " " << w << "\n";
    for (int x = 1; x <= h; ++x)
    {
        for(int y = 1; y <= w; ++y)
        {
            int aij = Random::Range(1, 100);
            std::cout << aij << " ";
            a[x][y] = aij;
        }
        
        std::cout << "\n";
    }

    int ans = 2 * h * w; // top + bottom
	
	for(int x = 1; x <= h; x++) {
		for(int y = 1; y <= w; y++) {
			for(int i = 0; i < 4; i++) {
				int x_ = x + dx[i];
				int y_ = y + dy[i];
				ans += std::max(0, a[x][y] - a[x_][y_]);
			}
		}
	}

    std::cerr << ans << "\n";
}