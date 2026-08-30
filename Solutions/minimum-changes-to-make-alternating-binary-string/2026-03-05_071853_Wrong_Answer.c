# Problem: Minimum Changes To Make Alternating Binary String
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-05_071853 UTC
# URL: https://leetcode.com/submissions/detail/1938491991/

int minOperations(char* s) {
    int operations = 0;
    for( int i=1 ; s[i]!='\0' ; i++ ){
       if( s[i] == s[i-1]){
           operations++;
           s[i] = s[i]^1;
       }
    }
    return operations;
}