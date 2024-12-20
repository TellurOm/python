#include<iostream>
using namespace std;
int main() {
    int r;
    int l;
    int h;
    cout<<"Enter the age of Ram : ";
    cin>>r;
    cout<<"Enter the age of Lakshman : ";
    cin>>l;
    cout<<"Enter the age of Hanuman : ";
    cin>>h;
    if (r<l and r<h)
    cout<<"Ram is the youngest.";
    else if (l<r and l<h)
    cout<<"Lakshman is the youngest.";
    else if (h<r and h<l)
    cout<<"Hanuman is the youngest.";
    else
    cout<<"Ram,Lakshman and Hanuman are of the same age.";
} 