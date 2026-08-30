# Problem: Fibonacci Number
# Status: Accepted
# Language: c
# Runtime: 6 ms
# Memory: 7.7 MB
# Submitted: 2026-02-08_140819 UTC
# URL: https://leetcode.com/submissions/detail/1912492903/



int fib(int n){
    if(n==0)
    return 0 ;
    else if ( n==1 )
    return 1 ;
    return fib(n-1)+fib(n-2);
}