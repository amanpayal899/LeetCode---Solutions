# Problem: Sqrt(x)
# Status: Accepted
# Language: c
# Runtime: 17 ms
# Memory: 8.4 MB
# Submitted: 2026-02-10_143501 UTC
# URL: https://leetcode.com/submissions/detail/1914743607/

int mySqrt(int x) {
    for(long long i = 1 ; ; i++){
        if(i*i > x)
        return --i;
        else if(i*i == x)
        return i ;
    }
    return 0;
}