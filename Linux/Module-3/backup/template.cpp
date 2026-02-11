#include <iostream>

template <typename T> void print(T value) { std::cout << value << std::endl; }
template <typename T> T max_val(T a, T b) { return (a>b)?a:b; }

int main() {
  std::cout<< "Max value: " << max_val(5,6)<<std::endl;
  return 0;
}
