bool isPowerOfFour(int n) {
    int flag=0;
    while(n>1 && ((n&1) == 0)){
        n>>=1;
        flag++;
    }
    if(n==1 && (flag%2==0))
    return true;
    else return false;
}
