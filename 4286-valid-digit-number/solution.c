bool validDigit(int n, int x) {
    int c=0;
    while(n!=0){
        if(n/10 == 0 && n==x )
            return false;
        else if(n%10 == x)
            c=1;
        n = n/10;
    }
    if( c==1 )
    return true;
    return false;
}
