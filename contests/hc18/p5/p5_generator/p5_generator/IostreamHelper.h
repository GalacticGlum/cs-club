#pragma once
#include <iostream>
#include <string>

class IostreamHelper
{
public:
	template<typename T>
	static T ReadInput(const std::string& prompt)
	{
		T v;
		std::cout << prompt;
		std::cin >> v;

		return v;
	}

};
