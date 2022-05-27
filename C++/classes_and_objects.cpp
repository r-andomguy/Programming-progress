#include <iostream>
#include <string>
using namespace std;

//creating class
class Person{
  public:
    string name;
    int id;
    void print(){
      cout<<"Name: "<<name<<" | "<<"ID: "<<id;
    }
    Person(string n, int i){ //constructor
      name=n; 
      id=i;
    }
};

class F{ //father
   public:
      int id_f = 00056;
};

class S: public F{ //son
    public:
      int id_s= 00019;
    void print(){
        cout<<"ID Son: "<<id_s<<endl;
        cout<<"ID Father: "<<id_f;
    }
    S(int x, int y){
        id_f=y;
        id_s=x;
        
      }
};

int main(){
  Person s1 = Person("bruno", 00001);
  s1.print();  
  Person s2 = Person("coelho", 00002);
  s2.print();
  Person s3 = Person("ribas", 00003);
  s3.print();
  S s4 = S(0011,0056);
  s4.print();
}