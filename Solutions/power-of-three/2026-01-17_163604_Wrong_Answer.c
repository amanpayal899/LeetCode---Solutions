# Problem: Power of Three
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-17_163604 UTC
# URL: https://leetcode.com/submissions/detail/1888020229/

bool isPowerOfThree(int n) {
    if(n==1) return 1;
    else if((n<3&&n>1)|| n<1) return 0;
    else {
         int r = isPowerOfThree(n/3);
         return r;
    }
}