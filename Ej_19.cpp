#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;
vector<int> singleNumber(vector<int>& nums) {
    vector<int> ans;
    unordered_map<int, bool> umap;
    for(int i =0; i < nums.size(); i++){
        if(umap.count(nums[i]))
            umap[nums[i]] = true;
        else
            umap[nums[i]] = false;
    }
    for(auto it = umap.begin(); it != umap.end(); ++it)
        if (it->second == true) 
            ans.insert(ans.begin(), it->first);
    return ans;
}
int main(){
    vector<int> nums = {1, 2, 3, 2, 1, 4, 5, 3, 6, 7, 8, 4, 8};
    vector<int> doubles = singleNumber(nums);
    for(int i: doubles)
        cout<<i << ", ";
    return 0;
}
