#include <iostream>
using namespace std;

int main(){
  //static array
  int x[5] = {0,1,2,3,4};
  cout<<"Static array: "<<x<<endl;

  //dinamic array
  int y[6];
  for(int i=0; i<6;i++){
    cout<<"Add an element in the array: ";
    cin>>x[i];
    }
  cout<<"Dinamic array: "<<y<<endl;
  
  //single dimensional array
  innt s_x[5] = {1,26,244,7,33};
  cout<<"Single dimensional array: "<<s_x<<endl;

  //multi dimensional array
  int md_y[2][3]= {{71,2,4},{854,234,5}};

  for(int i=0; i<2; i++){
    for(int j=0; j<5;j++){
      cout<<"Elements: "<<i<<" | "<<j<<" is "<<md_y[i][j]<<endl;
      }
  }  
}