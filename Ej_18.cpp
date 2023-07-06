#include <iostream>
#include <ctype.h>
using namespace std;
int main() {
    string ans;
    cout<< "Enter your name: "; getline(cin, ans);
    ans [0] = toupper(ans[0]);
    for(int i = 1; i < ans.length(); i++){
        if(isspace(ans[i-1]) && isalnum(ans[i]))
            ans[i] = toupper(ans[i]);
    }
    cout << ans;
    return 0;
}
