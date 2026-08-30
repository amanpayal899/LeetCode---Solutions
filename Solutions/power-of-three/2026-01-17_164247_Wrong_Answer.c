# Problem: Power of Three
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-17_164247 UTC
# URL: https://leetcode.com/submissions/detail/1888026913/

bool isPowerOfThree(float n) {
    if(n==1.0) return 1;
    else if((n<3&&n>1)|| n<1) return 0;
    else {
         int r = isPowerOfThree(n/3.0);
         return r;
    }
}