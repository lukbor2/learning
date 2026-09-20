#include <iostream>
#include <cmath>

using namespace std;

int main()
{
   float b, N, e;
    e = 0;
    cout<<"Enter the base of the power: ";
    cin>>b;
    cout<<"Enter the number to check: ";
    cin>>N;
    
    while(pow(b,e) < N){
        e++;
    }
    if (pow(b,e)==N){
        cout<<"Potenza trovata. "<<b<<"^"<<e<<"="<<N<<endl;
    }
    else
    {
        cout<<"Potenza NON trovata. "<<N<<" non e\' una Potenza di "<<b<<endl;
    }
    return 0;
}