#include <iostream>

int main()
{
	int i = 0;
	int sum = 0;
	int sum1 = 0;

	while (i < 101)
	{
		sum += i;
		sum1 += (i * i);
		i++;
	}
	sum *= sum;
	std::cout << (sum - sum1) << "\n";
	return 0;
}
