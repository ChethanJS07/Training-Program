#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
    vector<int>pairs;
    sort(potions.begin(), potions.end());
    for(int i=0;i<spells.size();i++){
      int low=0;
      int high=potions.size()-1;
      while(low<=high){
        int mid=low+(high-low)/2;
        if(spells[i]*potions[mid]>=success){
          high=mid-1;
        }
        else{
          low=mid+1;
        }
      }
      pairs.push_back(potions.size()-low);
    }
    return pairs;
  }
};

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  Solution obj;
  int n;
  cin>>n;
  vector<int> spells(n);
  for(int i=0;i<n;i++){
    cin>>spells[i];
  }
  int m;
  cin>>m;
  vector<int> potions(m);
  for(int i=0;i<m;i++){
    cin>>potions[i];
  }
  long long success;
  cin>>success;
  vector<int> res=obj.successfulPairs(spells,potions,success);
  for(int i=0;i<res.size();i++){
    cout<<res[i]<<" ";
  }
}
