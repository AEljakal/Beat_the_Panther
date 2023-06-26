#include <iostream>
#include <ctype.h>
using namespace std;
int num_of_words(string s){
	int num = 0;
	if(isalpha(s[0]))
		num++;
	for(int i =1; i <s.length()-1; i++)
		if(isspace(s[i]) && isalnum(s[i+1]))
			num++;
	if(isspace(s[s.length()-2]) && isalpha(s[s.length()]))
		num++;
	return num;
}
int main(){
	string s;
	cout<< "Enter a string: "; getline(cin, s);;
	cout<< "The string entered has " << num_of_words(s) << " words." << endl;
	
	return 0;
}
