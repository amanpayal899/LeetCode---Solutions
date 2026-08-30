# Problem: Power of Three
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-01-17_165500 UTC
# URL: https://leetcode.com/submissions/detail/1888039364/

bool isPowerOfThree(double  n) {
    if(n==1) return 1;
    else if(n<3) return 0;
    else {
         int r = isPowerOfThree(n/3.0);
         return r;
    }
}