#include <iostream>

int main()
{
	int sum = 0;
	int i = 0;

	while (i < 1000)
	{
		if ((i % 3 == 0) || (i % 5 == 0))
			sum += i;
		i++;
	}
	std::cout << sum << "\n";
	return 0;
}

// g++ -std=c++14 -Wall -Werror -Wextra pxxx.cpp -o pxxx
