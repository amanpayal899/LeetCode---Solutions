# Problem: Sqrt(x)
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-10_143409 UTC
# URL: https://leetcode.com/submissions/detail/1914742718/

int mySqrt(int x) {
    for(int i = 1 ; ; i++){
        if(i*i > x)
        return --i;
        else if(i*i == x)
        return i ;
    }
    return 0;
}