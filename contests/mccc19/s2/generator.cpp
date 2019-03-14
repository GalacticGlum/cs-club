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
const int MAXN = 22;
char grid[MAXN][MAXN];
int N;

bool is_horizontal(int i, char a)
{
    for (int j = 0; j < N; ++j)
    {
        if (grid[i][j] == a) continue;

        return false;
    }

    return true;
}

bool is_vertical(int j, char a)
{
    for (int i = 0; i < N; ++i)
    {
        if (grid[i][j] == a) continue;

        return false;
    }

    return true;
}

bool is_dig_1(char a)
{
    for (int i = 0; i < N; ++i)
    {
        if (grid[i][i] == a) continue;

        return false;
    }

    return true;
}

bool is_dig_2(char a)
{
    for (int i = 0; i < N; ++i)
    {
        if (grid[i][N - i - 1] == a) continue;

        return false;
    }

    return true;
}

int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

    std::string paramsArgument = std::string(argv[1]);
    std::vector<std::string> params = split(paramsArgument, " ");
    
    ull min = stoll(params[0]), max = stoll(params[1]);
    N = static_cast<int>(Random::Range(min, max));
    std::cout << N << "\n";
    for(int y = 0; y < N; ++y)
    {
        std::string row;
        for(int x = 0; x < N; ++x)
        {
            char c=Random::Value() <= 0.5f ? 'O' : 'X';
            row += c;
            grid[y][x]=c;
        }

        std::cout << row << "\n";
    }

    int x_count = is_dig_1('X') + is_dig_2('X');
    int o_count = is_dig_1('O') + is_dig_2('O');
    for (int i = 0; i < N; ++i)
    {
        if (is_horizontal(i, 'X')) ++x_count;
        if (is_horizontal(i, 'O')) ++o_count;
        if (is_vertical(i, 'X')) ++x_count;
        if (is_vertical(i, 'O')) ++o_count;
    }

    std::cerr << x_count << " " << o_count << "\n";
    if (x_count == o_count)
    {
        std::cerr << "Tie" << "\n";
    }
    else if (x_count > o_count)
    {
        std::cerr << "Joon" << "\n";
    }
    else
    {
        std::cerr << "Shon" << "\n";
    }
}