#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    if(!(n&(n-1)))
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}
