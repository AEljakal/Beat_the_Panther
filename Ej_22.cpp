#include <iostream>
using namespace std;
bool valid(string id){
	int sum =0;
	int nums[10];
	if(id.length() >10 || id.length() <10)
		return false;
	for(int i  = 0; i<10; i++){
		if(i%2 ==0)
			if(((id[i]-'0')*2) <9)
				sum+= (id[i]-'0')*2;
			else
				sum+= ((id[i]-'0')*2) - 9;
		else
			sum+= id[i] - '0';
	}
	if(10-sum%10 == id[9] - '0')
	return true;
	else
	return false;
}
int main(){
	string id;
	cout << "enter an id: "; getline(cin, id);
	if(valid(id))
    	cout << "The id: " << id << " is valid";
    else
    	cout << "The id: " << id << " is invalid";
    return 0;
}
