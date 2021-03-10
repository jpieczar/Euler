#include <iostream>

int main()
{
	int sum = 0;	
	int a = 1;
	int b = 2;
	int hold;

	while (b < 4000000)
	{
		if (b % 2 == 0)
			sum += b;
		hold = a;
		a = b;
		b += hold;
	}
	std::cout << sum << "\n";
	return 0;
}
