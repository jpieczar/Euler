#include <iostream>

int main()
{
	unsigned int i = 1;
	unsigned int j = 1;
	unsigned int tri = 0;
	int count = 0;

	while (true)
	{
		count = 0;
		j = 1;
		tri += i;
		while ((j * j) < tri)
		{
			if (tri % j == 0)
			{
				count++;
			}
			j++;
		}
		if ((count * 2) > 499)
		{
			std::cout << tri << "\n";
			break;
		}
		i++;
	}
	return 0;
}
