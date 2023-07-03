#include <iostream>
using namespace std;

int main(){
	int ans = rand()%100 +1;
	int in;
	for(int i =0; i <5; i++){
		cout<< "Enter your try: "; cin >> in;
		if(in == ans){
			cout<< "Correct you've WON";
			return 0;
		}else if(in > ans)
			cout<< "Your answer is greater than the correct answer" << endl;
		else if(in<ans)
			cout << "Your answer is lower than the correct answer" << endl;
	}
	cout << "You have used all of your 5 tries and you weren't able to guess the correct answer whitch is: " << ans << endl;
	return 0;
}
