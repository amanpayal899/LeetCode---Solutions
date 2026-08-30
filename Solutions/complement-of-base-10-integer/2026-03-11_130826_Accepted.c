# Problem: Complement of Base 10 Integer
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-03-11_130826 UTC
# URL: https://leetcode.com/submissions/detail/1945005916/

int bitwiseComplement(int n) {
    if ( n==0 )
      return 1;
    int temp = n;
    int mask=0;
    while( temp!=0)
    {
        temp = temp>>1;
        mask = (mask<<1)|1;
    }
    return n^mask ;
}