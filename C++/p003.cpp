#include <iostream>

typedef unsigned long long int ULLI;

int is_prime(ULLI n)
{
	ULLI i = 2;

	while ((i * i) <= n)
	{
		if (n % i == 0)
			return 0;
		i++;
	}
	return 1;
}

int main()
{
	ULLI n = 600851475143;
	ULLI i = 2;
	ULLI hold;
	
	while ((i * i) < n)
	{
		if (is_prime(i))
			if (n % i == 0)
			hold = i;
		i++;
	}
	std::cout << hold << "\n";
	return 0;
}
