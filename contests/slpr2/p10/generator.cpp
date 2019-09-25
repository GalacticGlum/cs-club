#include <iostream>
#include <numeric>
#include <string>
#include <random>
#include <ctime>
#include <vector>
#include <cmath>
#include <type_traits>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <fstream>
#include <exception>
#include <functional>

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

#define TESTCASE 5
#define MAXN 1000
#define MAXQ 1000000
#define MAXDIM 10
#define TESTCASE_PREFIX "p10.3."

// #define TESTCASE 10
// #define MAXN 1000
// #define MAXQ 100
// #define MAXDIM 3
// #define TESTCASE_PREFIX "p10.2."

// #define TESTCASE 10
// #define MAXN 100
// #define MAXQ 100
// #define MAXDIM 2
// #define TESTCASE_PREFIX "p10.1."


namespace kdt
{
	template <class PointT>
	class KDTree
	{
	public:
		KDTree() : root_(nullptr) {};
		KDTree(const std::vector<PointT>& points) : root_(nullptr) { build(points); }

		~KDTree() { clear(); }

		void build(const std::vector<PointT>& points)
		{
			clear();

			points_ = points;

			std::vector<int> indices(points.size());
			std::iota(std::begin(indices), std::end(indices), 0);

			root_ = buildRecursive(indices.data(), (int)points.size(), 0);
		}

		void clear()
		{ 
			clearRecursive(root_);
			root_ = nullptr;
			points_.clear();
		}

		bool validate() const
		{
			try
			{
				validateRecursive(root_, 0);
			}
			catch (const Exception&)
			{
				return false;
			}

			return true;
		}

		std::vector<int> knnSearch(const PointT& query, int k) const
		{
			KnnQueue queue(k);
			knnSearchRecursive(query, root_, queue, k);
			
			std::vector<int> indices(queue.size());
			for (size_t i = 0; i < queue.size(); i++)
				indices[i] = queue[i].second;

			return indices;
		}
	private:
		struct Node
		{
			int idx;       //!< index to the original point
			Node* next[2]; //!< pointers to the child nodes
			int axis;      //!< dimension's axis

			Node() : idx(-1), axis(-1) { next[0] = next[1] = nullptr; }
		};

		class Exception : public std::exception { using std::exception::exception; };

		template <class T, class Compare = std::less<T>>
		class BoundedPriorityQueue
		{
		public:

			BoundedPriorityQueue() = delete;
			BoundedPriorityQueue(size_t bound) : bound_(bound) { elements_.reserve(bound + 1); };

			void push(const T& val)
			{
				auto it = std::find_if(std::begin(elements_), std::end(elements_),
					[&](const T& element){ return Compare()(val, element); });
				elements_.insert(it, val);

				if (elements_.size() > bound_)
					elements_.resize(bound_);
			}

			const T& back() const { return elements_.back(); };
			const T& operator[](size_t index) const { return elements_[index]; }
			size_t size() const { return elements_.size(); }

		private:
			size_t bound_;
			std::vector<T> elements_;
		};


		using KnnQueue = BoundedPriorityQueue<std::pair<double, int>>;


		Node* buildRecursive(int* indices, int npoints, int depth)
		{
			if (npoints <= 0)
				return nullptr;

			const int axis = depth % PointT::DIM;
			const int mid = (npoints - 1) / 2;

			std::nth_element(indices, indices + mid, indices + npoints, [&](int lhs, int rhs)
			{
				return points_[lhs][axis] < points_[rhs][axis];
			});

			Node* node = new Node();
			node->idx = indices[mid];
			node->axis = axis;

			node->next[0] = buildRecursive(indices, mid, depth + 1);
			node->next[1] = buildRecursive(indices + mid + 1, npoints - mid - 1, depth + 1);

			return node;
		}


		void clearRecursive(Node* node)
		{
			if (node == nullptr)
				return;

			if (node->next[0])
				clearRecursive(node->next[0]);

			if (node->next[1])
				clearRecursive(node->next[1]);

			delete node;
		}


		void validateRecursive(const Node* node, int depth) const
		{
			if (node == nullptr)
				return;

			const int axis = node->axis;
			const Node* node0 = node->next[0];
			const Node* node1 = node->next[1];

			if (node0 && node1)
			{
				if (points_[node->idx][axis] < points_[node0->idx][axis])
					throw Exception();

				if (points_[node->idx][axis] > points_[node1->idx][axis])
					throw Exception();
			}

			if (node0)
				validateRecursive(node0, depth + 1);

			if (node1)
				validateRecursive(node1, depth + 1);
		}

		static double distance(const PointT& p, const PointT& q)
		{
			double dist = 0;
			for (size_t i = 0; i < PointT::DIM; i++)
				dist += (p[i] - q[i]) * (p[i] - q[i]);
			return sqrt(dist);
		}

	
		void knnSearchRecursive(const PointT& query, const Node* node, KnnQueue& queue, int k) const
		{
			if (node == nullptr)
				return;

			const PointT& train = points_[node->idx];

			const double dist = distance(query, train);
			queue.push(std::make_pair(dist, node->idx));

			const int axis = node->axis;
			const int dir = query[axis] < train[axis] ? 0 : 1;
			knnSearchRecursive(query, node->next[dir], queue, k);

			const double diff = fabs(query[axis] - train[axis]);
			if ((int)queue.size() < k || diff < queue.back().first)
				knnSearchRecursive(query, node->next[!dir], queue, k);
		}

		Node* root_;                 //!< root node
		std::vector<PointT> points_; //!< points
	};
} // kdt

class Point : public std::array<double, MAXDIM>
{
public:
	static const int DIM = MAXDIM;
	Point() {}
};

int main(int argc, char** argv) 
{
    Random::Initialize();
	std::vector<int> qValues = Random::UniformVector(1, MAXQ, TESTCASE);
    for(int ti = 0; ti < TESTCASE; ++ti)
    {
        std::ofstream input_file;
        std::ofstream output_file;
        input_file.open(TESTCASE_PREFIX + std::to_string(ti+1) + ".in");
        output_file.open(TESTCASE_PREFIX + std::to_string(ti+1) + ".out");

        int n = Random::Range(1, MAXN);
        int m = Random::Range(2, MAXDIM);
        int q = qValues[ti];

        input_file << n << " " << m << " " << q << "\n"; 

        std::vector<Point> points;
        for(int i = 0; i < n; ++i)
        {
            Point point;
            for(int j = 0; j < m; ++j)
            {
                point[j] = Random::Range(-10000, 10000);
                input_file << point[j] << " ";
            }

            input_file << "\n";
            points.push_back(point);
        }

        kdt::KDTree<Point> kdtree(points);
        for(int i = 0; i < q; ++i)
        {
			std::cout << i << "\n";
            int k = Random::Range(1, std::min(50, n));
            input_file << k << " ";

            Point point;
            for(int j = 0; j < m; ++j)
            {
                point[j] = Random::Range(-10000, 10000);
                input_file << point[j] << " ";
            }

            input_file << "\n";

            std::vector<int> indices = kdtree.knnSearch(point, k);
            
            Point sum;
            for(int i=0; i < m; ++i)
            {
                sum[i]=0;
            }
    
            for(auto& i : indices)
            {
                for(int j = 0; j < m; ++j)
                {
                    sum[j] += points[i][j];
                }
            }

            for(int i = 0; i < m; ++i)
            {
                output_file << sum[i] << " ";
            }

            output_file << "\n";
        }

        input_file.close();
        output_file.close();
		std::cout << "Done " << ti + 1 << "\n";
    }    
}