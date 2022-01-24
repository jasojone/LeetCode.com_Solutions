
//problem 
//https://leetcode.com/problems/sort-an-array/
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = sizeof(nums);
        sort(nums.begin(), nums.end());
        return nums;
    }
};