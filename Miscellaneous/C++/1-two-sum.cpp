#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;


class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> result;
        unordered_map<int, int> umap;

        for (int i = 0; i < nums.size(); i++){
            int numberToFind = target - nums[i];


            if(umap.find(numberToFind) != umap.end()){
                result.push_back(umap[numberToFind] + 1);
                result.push_back(i + 1);
                return result;
            }

            umap[nums[i]] = i;
       }

       return result;

    }
};