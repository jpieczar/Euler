#include <iostream>

typedef unsigned int UI;

int is_palindrome(UI start)
{
	UI end = 0;
	UI temp = start;

	// Fills end with the reverse of start.
	while (temp)
	{
		end *= 10;
		end += (temp % 10);
		temp /= 10;
	}
	if (end == start)
		return 1;
	return 0;
}

int main()
{
	UI i = 99;
	UI j = 99;
	UI hold = 0;

	while (i < 999)
	{
		j = i;
		while (j < 999)
		{
			if (is_palindrome(i * j))
				if ((i * j) > hold)

					hold = (i * j);
			j++;
		}
		i++;
	}
	std::cout << hold << "\n";
	return 0;
}
