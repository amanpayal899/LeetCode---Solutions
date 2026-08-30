# Problem: Power of Four
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 7.8 MB
# Submitted: 2026-01-27_153238 UTC
# URL: https://leetcode.com/submissions/detail/1898750829/

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