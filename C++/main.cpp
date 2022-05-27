#include <iostream>
using namespace std;

int glob=10; //global variable

void print(){
  cout<<glob<<endl;
}

int main(){
  print();

  glob=100;
  cout<<"Now the global variable is: ";
  print();
  
}

