#include <vector>
#include <numeric>
#include <algorithm>
#include <exception>
#include <functional>
#include <iostream>
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

#define MAXDIM 50
class Point : public std::array<int, MAXDIM>
{
public:
	static const int DIM = MAXDIM;
	Point() {}
};

int main()
{
    std::ios_base::sync_with_stdio(NULL);
    std::cout.tie(0);
    std::cin.tie(0);
    
    int n,m,q,x;
    std::cin >> n >> m >> q;
    
    std::vector<Point> points;
    for (int i = 0; i < n; ++i)
    {
        Point point;
        for (int j = 0; j < m; ++j)
        {
            std::cin>>x;
            point[j]=x;
        }
        
        points.push_back(point);
    }
    
    kdt::KDTree<Point> kdtree(points);
    for(int i = 0; i < q; ++i)
    {
        Point p;
        int k;
        std::cin>>k;
        for(int j = 0; j < m; ++j)
        {
            std::cin>>x;
            p[j]=x;
        }
        
        std::vector<int> indices = kdtree.knnSearch(p, k);
        Point sum;
        for(int i=0; i < m; ++i) {
            sum[i]=0;
        }
        
        for(auto& i : indices)
		{
			for(int j = 0; j < m; ++j)
			{
				sum[j] += points[i][j] % 1000000007;
			}
		}

		for(int i = 0; i < m; ++i)
		{
			std::cout << sum[i] << " ";
		}

		std::cout << "\n";
    }
}