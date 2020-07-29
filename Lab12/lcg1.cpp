#include<bits/stdc++.h>
using namespace std;

double f(const double& x){
	return x*x;
}

int main(){
int n=0;
double sum=0, x=0, y=0;
srand(time(NULL));
cout << "What value of n do you wish to use the algorithm for?" << endl;
cin >> n;

for(int i; i<n; i++)
{
	while(true)
	{
		x = static_cast<double>(rand()) / RAND_MAX;
		if(x<=1 && x>=0)
		{
			break;
		}
	}
	
	cout << x << endl;
	sum += f(x);
}

sum = sum / n;
cout << "Value of the integral you wish to calculate is : " << sum << endl;
}
