#include <iostream>
#include <vector>
#include <ctype.h>

using namespace std;

bool password(string s){
	if(s.length()<8)
		return false;
	bool cap, small, num;
	for(char i: s){
		if(isspace(i))
			return false;
		else if(islower(i))
			small = true;
		else if(isupper(i))
			cap = true;
		else if(isdigit(i))
			num = true;
	}
	return (cap && small && num);
}

int main() {

	cout << password("Hilkajdsfla kjfsdlkasjdf6")<<endl;
	return 0;
}