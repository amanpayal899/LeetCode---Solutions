# Problem: Minimum Changes To Make Alternating Binary String
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9 MB
# Submitted: 2026-03-05_075300 UTC
# URL: https://leetcode.com/submissions/detail/1938519888/

int minOperations(char* s) {
    int p1 = 0;int i=0;
    for(  ; s[i]!='\0' ; i++ ){
        if( i%2 == 0 && s[i] != '0'){
           p1++;
        }
        else if( i%2 == 1 && s[i] != '1')
           p1++;
    }
    if( p1<i-p1)
    return p1;
    return i-p1;
}