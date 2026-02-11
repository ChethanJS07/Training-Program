#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string removeStars(string s) {
    string out;
    stack<char>stk;

    for(int i=0;i<s.size();i++){
      if(s[i]=='*'){
        stk.pop();
      }
      else{
        stk.push(s[i]);
      }
    }
    while(!stk.empty()){
      out.push_back(stk.top());
      stk.pop();
    }
    reverse(out.begin(),out.end());
    return out;
  }    
};

int main(){
  Solution obj;
  string s;
  cin>>s;
  cout<<obj.removeStars(s);
}
