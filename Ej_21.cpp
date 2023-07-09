#include <iostream>
using namespace std;
int main(){
    
    int mat1[2][3] = {
		{2, 4, 5},
		{1, 3, 6}
	};
	int mat2[3][2];
	for(int i = 0; i < 3; i++){
		for(int j =0; j <2; j++){
			mat2[i][j] = mat1[j][i];
			cout << mat2[i][j] << "\t";
		}
	cout << endl;
	}
    return 0;
}
