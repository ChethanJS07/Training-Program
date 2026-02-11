#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  int minimizeArrayValue(vector<int> &nums) {
    long long sum = nums[0];
    long long res = nums[0];

    for (int i = 1; i < nums.size(); i++) {
      sum += nums[i];
      res = max(res, (sum + i) / (i + 1));
    }
    return res;
  }
};

int main() {
  Solution obj;
  int n;
  cin >> n;
  vector<int> nums(n);
  for (int i = 0; i < n; i++) {
    cin >> nums[i];
  }
  cout << obj.minimizeArrayValue(nums);
}
