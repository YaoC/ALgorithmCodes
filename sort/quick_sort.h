void swap(int& a,int& b){
    int temp = a;
    a = b;
    b = temp;
}

int partition(int* array,int p,int r){
    int x = array[p];
    p++;
    while(1){
        for(;array[p]<=x&&p<=r;p++);
        for(;array[r]>x;r--);
        if(p>r)
            return r;
        swap(array[p],array[r]);
    }
}

void qsort(int* array,int p,int r){
    if(p<r){
        int q = partition(array,p,r);
        swap(array[p],array[q]);
        qsort(array,p,q-1);
        qsort(array,q+1,r);
    }
}


