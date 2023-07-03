#include <iostream>
using namespace std;

int main(){
	int a=0, b=0;
	int arr[3][2] = {
		{2,3},
		{-1,5},
		{4,-2}	
	};
	for(int i = 0; i <3; i++)
		a+=arr[i][0];
	for(int j = 0; j<3; j++){
		b+=arr[j][1];
	}
	cout<<"The final coordinates are (" << a  << "," << b << ")" << endl;
	return 0;
}
