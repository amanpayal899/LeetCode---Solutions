# Problem: Reverse Bits
# Status: Accepted
# Language: c
# Runtime: 2 ms
# Memory: 8.8 MB
# Submitted: 2026-04-29_130943 UTC
# URL: https://leetcode.com/submissions/detail/1991030925/

int reverseBits(int n) {
    int rev = 0;
    for( int i=0; i<32; i++ )
    {
        
        rev = rev << 1;
        rev = rev | (n&1);
        n = n >> 1;
    }
    return rev;

}