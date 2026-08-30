# Problem: Power of Two
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 7.8 MB
# Submitted: 2026-01-28_175611 UTC
# URL: https://leetcode.com/submissions/detail/1900116202/

bool isPowerOfTwo(int n) {
   
    while(n>1 && ((n&1 )== 0)){
        n>>=1;
       
    }
    if(n==1) return true;
    else return false;
}