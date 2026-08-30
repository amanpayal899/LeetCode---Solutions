# Problem: Pow(x, n)
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-30_151329 UTC
# URL: https://leetcode.com/submissions/detail/1902105355/

double myPow(double x, int n) {
    if( n == 0)
    return 1 ; 
    double result ;
    if(n>0){
        result = x * myPow(x,n-1);   
    }
    else{ 
       
       result = (1/x)*(myPow(x,n+1));
    }
    return result ;
}