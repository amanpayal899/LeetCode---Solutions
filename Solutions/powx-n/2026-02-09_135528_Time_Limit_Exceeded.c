# Problem: Pow(x, n)
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-09_135528 UTC
# URL: https://leetcode.com/submissions/detail/1913532169/

double myPow(double x, int n) {
    double result = 1 ;
    if(n == 0)
    return 1;
    if ( n<0 ){
        while ( n!=0 ){
          result *= x ;
          n++;
        }
        result = 1.0/result ;
    }
    else if( n>0 ){
        while( n!=0 ){
            result *= x ;
            n--;
        }
    }
    return result ;
}