#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <limits>

int main(int argc, char** argv)
{
    int inf = std::numeric_limits<int>::max();

    std::string judge_input_filename = argv[1];
    std::string process_output_filename = argv[2];

    // Read the judge input and process output
    std::ifstream judge_input_file(judge_input_filename);
    std::ifstream process_output_file(process_output_filename); 

    int k;
    process_output_file >> k;

    int n;
    std::string data_input;

    judge_input_file >> n;
    std::vector<int> original_data(n);
    for (int i = 0; i < n; ++i)
    {
        judge_input_file >> data_input;
        if (data_input == "X")
        {
            original_data.push_back(inf);
        }
        else
        {
            original_data.push_back(std::stoi(data_input));
        }
    }

    int x;
    std::vector<int> shifted_data(n);
    for (int i = 0; i < n; ++i)
    {
        judge_input_file >> x;
        shifted_data.push_back(x);
    }

    judge_input_file.close();
    process_output_file.close();

    bool result = true;
    for (int i = 0; i < n; ++i)
    {
        if (original_data[i] == inf) continue;
        if (original_data[i] != shifted_data[(i + k) % n])
        {
            result = false;
            break;
        }
    }

    return static_cast<int>(!result);
}