#include <iostream>
#include <climits>

int check_num(int num)
{
	int i = 2;

	while (i < 21)
	{
		if (num % i != 0)
			return 0;
		i++;
	}
	return 1;
}

int main()
{
	int i = (INT_MAX / 10);

	while (i < INT_MAX)
	{
		if (check_num(i))
		{
			std::cout << i << "\n";
			return 0;
		}
		i++;
	}
	return 0;
}
