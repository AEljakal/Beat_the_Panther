#include <iostream>
using namespace std;
int main(){
    int sums, ac_sums = 0, size;
    int nums[] = {12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23};
    for(int i:nums)
        ac_sums+=i;
    size = sizeof(nums)/sizeof(nums[0]) + 1;
    sums = size/2*(nums[0]+nums[size-2]);
    cout << "The missing element is: " << sums - ac_sums;
    return 0;
}
