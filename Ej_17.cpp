#include <iostream>
#include <regex>
using namespace std;
bool ValidationOfRomanNumerals(string str){

    const regex pattern("^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$");
    if (str.empty()) {
        return false;
    }
    if (regex_match(str, pattern)) {
        return true;
    }
    else {
        return false;
    }
}

int main(){
    string str;
    cout<< "Enter a roman numeral: "; getline(cin, str);
    cout << ValidationOfRomanNumerals(str) << endl;
    return 0;
}
