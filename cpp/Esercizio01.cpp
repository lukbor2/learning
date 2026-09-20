#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double b, e, p;
    cout<<"Inserisci la base della potenza: ";
    cin>> b;
    e=0;
    p=0;
    while(e<10){
        p=pow(b,e);
        cout<<"La potenza con base "<<b<<"e esponente "<<e<<": "<<p<<endl;
        e++;
    }

    return 0;
}

