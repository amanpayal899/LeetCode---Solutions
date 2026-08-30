# Problem: Pow(x, n)
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 7.9 MB
# Submitted: 2026-02-09_153345 UTC
# URL: https://leetcode.com/submissions/detail/1913634511/

double myPow(double x, int n) {
    if(n==0 || x==1 )
    return 1;
    long long N = n ;
    double result = 1 ;
    if(n<0){
      x = 1/x ;
       N = -N ;
    }
    while( N>0 ){
        if( (N&1) != 0 )
            result *= x ;
        x *= x ;
        N >>= 1;
    }
    return result ;
}