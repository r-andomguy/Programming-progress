#include <iostream>
using namespace std;

int main(){
  int age;
  cout<<"Enter your age for vaccination: ";
  cin>>age;

  if(age>=10){
    cout<<"Eligible for vaccination";
  }
  else if(age>=200){
    cout<<"Are you alive?";
  }
  else{
    cout<<"You're not eligible.";
  }
}

