# Problem: Pow(x, n)
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-09_151135 UTC
# URL: https://leetcode.com/submissions/detail/1913610898/

double myPow(double x, int n) {
    double result = 1 ;
    if(n<0){
      x = 1/x ;
      n = -n  ;
    }
    while( n!=0 ){
        if( (n&1) != 0 )
            result *= x ;
        x *= x ;
        n >>= 1 ;
    }
    return result ;
}