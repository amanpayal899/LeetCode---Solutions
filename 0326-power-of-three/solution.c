bool isPowerOfThree(double  n) {
    if(n==1) return 1;
    else if(n<3) return 0;
    else {
         int r = isPowerOfThree(n/3.0);
         return r;
    }
}
