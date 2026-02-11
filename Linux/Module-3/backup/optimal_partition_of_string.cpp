#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
  int partitionString(string s) {
    string res;
    int count=1;
    for(int i=0;i<s.size();i++){
      if(res.find(s[i])==-1){
        res.push_back(s[i]);
      }
      else{
        res.clear();
        res.push_back(s[i]);
        count++;
      }
    }
    return count;
  }
};

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  Solution obj;
  string s;
  cin>>s;
  cout<<obj.partitionString(s)<<endl;
}
