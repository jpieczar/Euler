#include <iostream>

int is_prime(int num)
{
	int i = 2;

	while ((i * i) <= num)
	{
		if (num % i == 0)
			return 0;
		i++;
	}
	return 1;
}

int main()
{
	int i = 0;
	int j = 0;

	while (j < 10002)
	{
		i++;
		if (is_prime(i))
			j++;
	}
	std::cout << i << "\n";
	return 0;
}
