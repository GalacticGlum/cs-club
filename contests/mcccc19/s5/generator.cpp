#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>
#include <bits/stdc++.h>

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
#define endl "\n"
#define INF 0x3f3f3f3f
#define pii pair<int, int>
#define pb push_back
#define f first
#define s second
#define MEM(a, b) memset(a, b, sizeof(a))
#define forn(i, n) for (int i = 0; i < n; ++i)
typedef long long ll;

std::vector<int> stateMask;
const int MAXN = 12;
int N, K;
ll dp[MAXN][MAXN * MAXN][1 << MAXN];
int maskCount[1 << MAXN];

int countMask(int mask)
{
    int counter = 0;

    for (int i = 0; i < MAXN; ++i)
    {
        if (mask & (1 << i)) ++counter;
    }

    return counter;
}

void init()
{
    MEM(dp, 0);

    for (int i = 0; i < (1 << N); ++i)
    {
        if (!(i & (i << 1)))
        {
            stateMask.pb(i);
            maskCount[i] = countMask(i);
        }
    }
}
int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

    int n = Random::Range(1, 10);
    int k = Random::Range(0, n*n);
    std::cout << n << " " << k << "\n";
    init();

    forn(i, stateMask.size())
    {
        int mask = stateMask[i];
        ++dp[1][maskCount[mask]][mask];
    }

    for (int n = 2; n <= N; ++n)
    {
        for (int k = 0; k <= K; ++k)
        {
            forn(i, stateMask.size())
            {
                forn(j, stateMask.size())
                {
                    int current = stateMask[i];
                    int past = stateMask[j];

                    if (k - maskCount[current] < 0) continue;

                    int hits = past | (past << 1) | (past >> 1);

                    if (hits & current) continue;

                    dp[n][k][current] += dp[n - 1][k - maskCount[current]][past];
                }
            }
        }
    }

    ll total = 0;

    forn(i, stateMask.size())
    {
        total += dp[N][K][stateMask[i]];
    }

    std::cerr << total << "\n";
}