#include <iostream>

int main()
{
	int a = 3;
	int b = 4;
	int c = (1000 - (a + b));

	while (a < 999)
	{
		b = (a + 1);
		while (b < 999)
		{
			c = (1000 - (a + b));
			if ((a*a) + (b*b) == (c*c))
				if ((a + b + c) == 1000)
				{
					std::cout << (a * b * c) << "\n";
					return 0;
				}
			b++;
		}
		a++;
	}
	return 0;
}
