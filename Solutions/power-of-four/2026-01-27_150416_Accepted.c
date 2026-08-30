# Problem: Power of Four
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.1 MB
# Submitted: 2026-01-27_150416 UTC
# URL: https://leetcode.com/submissions/detail/1898718231/

bool isPowerOfFour(float n) {
    if(n==1)
    return 1;
    else if(n < 4)
    return 0;
    return n=isPowerOfFour(n/4.0);
}