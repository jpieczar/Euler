#include <iostream>

typedef unsigned long long int ULLI;

int is_prime(ULLI num)
{
	ULLI i = 2;

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
	ULLI i = 2;
	ULLI sum = 0;

	while (i < 2000000)
	{
		if (is_prime(i))
			sum += i;
		i++;
	}
	std::cout << sum << "\n";
	return 0;
}
