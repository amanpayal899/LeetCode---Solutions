# Problem: Pow(x, n)
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.3 MB
# Submitted: 2026-02-09_154227 UTC
# URL: https://leetcode.com/submissions/detail/1913644246/

double myPow(double x, int n) {
    if(n==0 || x==1 )
    return 1;
    long long *ptr = (long long *)malloc(sizeof(long long)) ;
    *ptr = n ;
    double result = 1 ;
    if(n<0){
      x = 1/x ;
      *ptr= -(*ptr) ;
    }
    while( (*ptr)>0 ){
        if( ((*ptr)&1) != 0 )
            result *= x ;
        x *= x ;
        (*ptr) >>= 1;
    }
    free(ptr) ;
    return result ;
}