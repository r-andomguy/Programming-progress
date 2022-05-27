#include <iostream>
using namespace std;

//addition function
int add(int x, int y){
  return x + y;
}
double add(double x, double y){
  return x * y;
}

int main(){
  cout<<"Sum: "<<add(5,10)<<endl;
  cout<<"Times: "<<add(5.34,10.99)<<endl;
}

