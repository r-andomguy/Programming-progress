#include <iostream>
using namespace std;

//addition function
int add(int x, int y){
  return x + y;
}

//subtraction function
int sub(int x, int y){
  return x - y;
}

//multiplication function
int mul(int x, int y){
  return x * y;
}

//divided function
int d(int x, int y){
  return x / y;
}

//percent function
int p(int x, int y){
  return x % y;
}

int main(){
  cout<<"Sum: "<<add(5,10)<<endl;
  cout<<"Minus: "<<sub(5,10)<<endl;
  cout<<"Times: "<<mul(5,10)<<endl;
  cout<<"Divided: "<<d(5,10)<<endl;
  cout<<"Percent: "<<p(5,10)<<endl;
}

