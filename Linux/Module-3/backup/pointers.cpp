#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

void birthday(int* age){
  (*age)++;
}
int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  int age = 25;
  printf("%p\n", &age);
  int* age_ptr = &age;
  printf("%p\n", age_ptr);

  birthday(&age);
  printf("%d\n", age);

  return 0;
}
