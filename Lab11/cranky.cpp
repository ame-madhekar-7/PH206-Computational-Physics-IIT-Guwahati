#include <bits/stdc++.h>
#include <fstream>
using namespace std;

float fun(float x, float l){
	return x*(l-x);
}

int main(){
int i, j, m, n;
float A, B, l, t, D;
A = 0.4; B = 0.1; l = 1.2; t = 30.0, D = 0.2; 
float al = D*B / (2*A*A);

m = 1 + l/A;
n = t/B;

float u[m]; float g[m-2][m-2]; float uu[m-2]; float e[m-2]; float d[m-2]; float b[m-2]; float a[m-2]; float c[m-3];

u[0] = 0.0;
u[m-1] = 0.0; 

for(i=0; i<m-1; i++){
u[i] = fun(A, l);
A += 0.4;
}

for(i=0; i<m-4; i++){
uu[i] = u[i+1];
}

for(i=0; i<m-2; i++)
{
	for(j=0; j<m-2; j++)
	{
		g[i][j] = 0.0;
	}
}

for(i=0; i<m-2; i++)
{
	g[i][i] = 1-2*al;
	g[i][i+1] = al;
	g[i+1][i] = al;
}

for(i=0; i<m-2; i++)
{
	e[i] = 0.0;	
}

e[0] = 2*al*u[0];
e[m-3] = 2*al*u[m-1];

for(int l=0; l<n; l++)
{
	for(i=0; i<m-2; i++)
	{
		float sum=0.0;
		for(j=0; j<m-2; j++)
		{
			sum += g[i][j] * uu[j];
		}	
	d[i] = sum + e[i];
	}
	
	for(i=0; i<m-2; i++)
	{
		b[i] = 1+2*al;
	}
		
	for(i=0; i<m-3; i++)
	{
		c[i] = -al;
		a[i+1] = -al;
	}
		
	for(i=0; i<m-3; i++)
	{
		if(i==0)
		{
			c[i] = c[i] / b[i];
			d[i] = d[i] / b[i];
		}
		else
		{
			c[i] = c[i] / (b[i] - a[i]*c[i-1]);
			d[i] = (d[i] - a[i]*d[i-1]) / (b[i] - a[i]*c[i-1]);
		}
		
	d[m-3] = (d[m-3] - a[m-3]*d[m-4]) / (b[m-3] - a[m-3]*c[m-4]);
	uu[m-3] = d[m-3];
			
	for(i=m-4; i>=0; i--)
	{
		uu[i] = d[i] - c[i]*uu[i+1];
	}
	for(i=0; i<m-2; i++)
	{
		u[i+1] = uu[i];
	}
		
	ofstream f;
	f.open("1.txt");
	for(i=0; i<m; i++)
	{
		A = i*0.4;
		f << A << " " << u[i] << endl;
	}
	f.close();
	}
	return 0;
}
}
		
		
		
		
		
		
		
		
		




















