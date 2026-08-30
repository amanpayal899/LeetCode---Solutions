# Problem: Number of 1 Bits
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.9 MB
# Submitted: 2026-08-05_194652 UTC
# URL: https://leetcode.com/submissions/detail/2095852712/

int hammingWeight(int n) {
    int cpy = n;
    int count = 0;
    while( cpy>0){
        cpy = cpy & (cpy-1);
        count ++;
    }
    return count;
}