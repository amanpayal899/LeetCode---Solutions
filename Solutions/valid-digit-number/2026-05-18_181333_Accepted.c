# Problem: Valid Digit Number
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-05-18_181333 UTC
# URL: https://leetcode.com/submissions/detail/2006642402/

bool validDigit(int n, int x) {
    int c=0;
    while(n!=0){
        if(n/10 == 0 && n==x )
            return false;
        else if(n%10 == x)
            c=1;
        n = n/10;
    }
    if( c==1 )
    return true;
    return false;
}