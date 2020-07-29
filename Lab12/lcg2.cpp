#include<bits/stdc++.h>
using namespace std;

double fun(double x){
	return ((x*x)*x - x);
}

int main(){
int n, j;
int m = 714025, a = 1366, c = 150889, i = 2, f = 5;
cout << "What value of n do you wish to use the algorithm for?" << endl;
cin >> n;
int x[n];
double u[n];
x[0] = 1;

for(int j=0; j<n-1; j++)
{
	x[j+1] = (a*x[j] + c) % m;
}

for(int j=0; j<n; j++)
{
	u[j] = (double) x[j] / m;
	cout << u[j] << endl;
}

int size = sizeof(u) / sizeof(u[0]);
unsigned seed = 0;
random_shuffle(u, u+size);
double sum = 0;

cout << "shuffled set of random numbers : " << endl;
for(int j=0; j<n; j++)
{
	cout << "u[j] = " << u[j] << endl;
	double d = u[j] * ((double)f - (double)i) + (double)i;
	cout << "d = " << d << endl;
	sum = sum + fun(d);
}

sum = sum * (f-i)/n;

cout << "Value of the integral you wish to calculate is : " << sum << endl;
}
