
#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double n, r, base, somma, e;
    cout<<"Inserisci il numero n: ";
    cin>>n;
    cout<<"Inserisci l'esponente: ";
    cin>>e;
    r=0;
    base=1;
    somma=0;
    while (base<=n)
    {
        r = pow(base,e);
        somma = somma + r;
        base++;
    }

    cout<<"La somma dei quadrati : "<<somma<<endl;

    return 0;
}