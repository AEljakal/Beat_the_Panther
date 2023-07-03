#include <iostream>
#include <vector>
using namespace std;

int win(vector<int>& val){
	int max = val[0];
	int ans = 0;
	for(int i = 1; i <3; i++)
		if(val[i]>max){
			max = val[i];
			ans = i;
		}
	return ans+1;
}
int main(){
	vector<int> values;
	int in;
	for(int i = 0; i <3; i++){
		cout<< "Enter the speed if the turtle No. " << i+1 << " :";
		cin >> in;
		values.push_back(in);
	}
	cout << "The winning turtle is the turtle No. " << win(values)<<endl;
	return 0;
}
