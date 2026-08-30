# Problem: Number Complement
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.4 MB
# Submitted: 2026-03-12_133721 UTC
# URL: https://leetcode.com/submissions/detail/1946051582/

int findComplement(int num) {
    int cpy_num = num ;
    int mask = 1 ;
    if( num == 0)
      return 1;
    while ( cpy_num > 1)
    {
        cpy_num = cpy_num >> 1 ;
        mask = mask << 1 ;
        mask++ ;
    }
    return num^mask ;
}