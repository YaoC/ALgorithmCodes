#include <iostream>
#include "./quick_sort.h"

using namespace std;

int main() {
    int test[] = {27,99,0,8,13,64,86,16,7,10,88,25,90};
    qsort(test,0,12);
    for(auto i:test)
        cout<<i<<" ";
    return 0;
}