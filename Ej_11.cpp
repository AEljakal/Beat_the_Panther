#include <iostream>
#include <ctype.h>
#include <string>
using namespace std;

string decrypt(string s){
	char code[] = {'m','u','r','c','i','e','l','a','g','o'};
	for(int i =0; i < s.length(); i++)
		if(isdigit(s[i]))
			s[i] = code[s[i]-'0'];
	return s;
}
int main(){
	cout << decrypt("T24st5z7 S9y y9 d5 n15v9 H735 t450p9 q15 n9s v509s N9 p92q15 q14527 p529 b15n9 1st5d s450p25 05 q14s9 0as") << endl;
	return 0;
}
