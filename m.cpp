
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
   int i,j,h,n,x,t,sum;
   sum=0;
   j=0;
   h=0;

   cin >> t;
   while(t--)  {
   cin >> n;
   vector<int>tab;

   for (i=0;i<n;i++){
    cin >> x;
    tab.push_back(x);

   }
   vector<int> b;
   while(sum == 0 && h <n && j < n){
            if(sum!=0  ){
            if (j !=h){
            sum+=tab[h];
            b.push_back(tab[h]);
            h++;}
            }else{
                j++;
                h=j;
                b.clear();
            }

            }

     for (i = 0; i<n;i++){
        cout << b[i] << " ";

     }
   }


   }

