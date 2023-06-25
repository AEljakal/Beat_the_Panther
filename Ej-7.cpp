#include <iostream>
#include <ctype.h>
using namespace std;
bool v_Email(string s){
	bool name = 0, domain = 0, extension = 0, at = 0, dot = 0;
	for(char i:s){
		if(isspace(i))
			return false;
		if(i == 64)
			at = true;
		if(i == 46)
			dot = true;
		if(isalpha(i)){
			if(!at)
				name = true;
			if(at&&!dot)
				domain = true;
			if(dot)
				extension = true;
		}
	}
	return (name&&domain&&extension);
}
int main(){
	string s;
	cout<< "Enter an E-mail address: "; cin >> s;
	if(v_Email(s))
		cout << "Valid E-mail.";
	else
		cout<< "Invalid E-mail.";
	return 0;
}
