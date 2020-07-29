
#include <bits/stdc++.h>
using namespace std;
#include <fstream>

# define h 0.25

int main()
{
	int i, j;
	int m, n;
	int k = 0.0;
	int counter = 0;
	float a, b;
	a = 1.0;
	b = 1.0;
	m = 1 + b/h;
	n = 1 + a/h;
	
	float phi[m][n];
	
	for(i=1; i<m-1; i++)
		{
			for(j=1; j<n-1; j++)
				phi[i][j] = 0.0;
		}
	
	for(j=1; j<n-1; j++)
	{
		phi[0][j] = 0.0;
		phi[m-1][j] = 0.0;
	}
	for(i=1; i<m-1; i++)
	{
		phi[i][0] = 0.0;
		phi[i][n-1] = k;
	}
	
	while(counter<10)
		{
		counter++;
		for(i=1; i<m-1; i++)
			{
				for(j=1; j<n-1; j++)
					{
						phi[i][j] = (phi[i+1][j] + phi[i-1][j] + phi[i][j+1] + phi[i][j-1] - h*h) / 4.0;
						cout << i << " " << j << " " << phi[i][j] << endl;
					}
			}
		}
	
}
	
	
	
	
	
	
