bool isPowerOfTwo(int n) {
   
    while(n>1 && ((n&1 )== 0)){
        n>>=1;
       
    }
    if(n==1) return true;
    else return false;
}
