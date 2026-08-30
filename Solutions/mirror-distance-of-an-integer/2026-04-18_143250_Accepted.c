# Problem: Mirror Distance of an Integer
# Status: Accepted
# Language: c
# Runtime: 4 ms
# Memory: 9.1 MB
# Submitted: 2026-04-18_143250 UTC
# URL: https://leetcode.com/submissions/detail/1981806997/

int mirrorDistance(int n) {
    int rev = 0;
    int temp = n;
    while(temp>0){
        rev = rev*10 + temp%10;
        temp = temp/10;
    }
    if( rev > n )
        return rev-n;
    return n-rev;
}