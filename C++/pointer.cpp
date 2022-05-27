#include <iostream>
using namespace std;

int main(){
  int x = 10;
  int *ptr; //pointer 

  ptr=&x; //pointer == x address
  cout<<"X address: "<<ptr<<endl;
  cout<<"Pointer value: "<<*ptr<<endl;
  cout<<"X value: "<<x;
}