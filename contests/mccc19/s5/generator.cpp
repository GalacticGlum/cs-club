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

#include <stack>
using namespace std;
struct SuffixArray {
 const int L;
 string s;
 vector<vector<int> > P;
 vector<pair<pair<int,int>,int> > M;
 SuffixArray(const string &s) : L(s.length()), s(s), P(1, vector<int>(L, 0)), M(L) {
   for (int i = 0; i < L; i++) P[0][i] = int(s[i]);
   for (int skip = 1, level = 1; skip < L; skip *= 2, level++) {
     P.push_back(vector<int>(L, 0));
     for (int i = 0; i < L; i++)
M[i] = make_pair(make_pair(P[level-1][i], i + skip < L ? P[level-1][i + skip] : -1000), i);
     sort(M.begin(), M.end());
     for (int i = 0; i < L; i++)
P[level][M[i].second] = (i > 0 && M[i].first == M[i-1].first) ? P[level][M[i-1].second] : i;
   }    
 }
 vector<int> GetSuffixArray() { return P.back(); }
 // returns the length of the longest common prefix of s[i...L-1] and s[j...L-1]
 int LongestCommonPrefix(int i, int j) {
   int len = 0;
   if (i == j) return L - i;
   for (int k = P.size() - 1; k >= 0 && i < L && j < L; k--) {
     if (P[k][i] == P[k][j]) {
i += 1 << k;
j += 1 << k;
len += 1 << k;
     }
   }
   return len;
 }
};
vector<int> hist;
int getMaxArea()
{
int n = hist.size();
   stack<int> s;
   int max_area = 0;
   int tp;
   int area_with_top;
   int i = 0;
   while (i < n)
   {
       if (s.empty() || hist[s.top()] <= hist[i])
           s.push(i++);
       else
       {
           tp = s.top();  // store the top index
           s.pop();  // pop the top
           area_with_top = hist[tp] * (s.empty()  ? i+1 : i - s.top() );
           if (max_area < area_with_top)
               max_area = area_with_top;
       }
   }
   while (s.empty() == false)
   {
       tp = s.top();
       s.pop();
       area_with_top = hist[tp] * (s.empty() ? i+1 : i - s.top() );
       if (max_area < area_with_top)
           max_area = area_with_top;
   }
   return max_area;
}

int main(int argc, char** argv) 
{
    std::ios_base::sync_with_stdio(NULL);
    std::cout.tie(0);
    std::cin.tie(0);

    Random::Initialize();
    std::string str = Random::String(Random::Range(1, 100000));
    std::cout << str << "\n";

    SuffixArray suffix(str);
    vector<int> v = suffix.GetSuffixArray();
    int a[str.length()];

    for (int i = 0; i < v.size(); i++)
    a[v[i]] = i;
    for(int i=0 ; i< str.length() - 1 ; i++)
    {
    hist.push_back(suffix.LongestCommonPrefix(a[i], a[i+1]));
    }

    int temp = getMaxArea();
    if(temp > str.length() )
    cerr<<temp<<"\n";
    else
    cerr<<str.length()<<"\n";
}