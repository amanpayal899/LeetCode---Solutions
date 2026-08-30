# Problem: Count Binary Substrings
# Status: Accepted
# Language: c
# Runtime: 2 ms
# Memory: 9 MB
# Submitted: 2026-02-20_010958 UTC
# URL: https://leetcode.com/submissions/detail/1924894053/

#pragma GCC optimize("O3, unroll-loops")
int countBinarySubstrings(char* s) {
    int prev=0, cur=1, cnt=0;
    for (int i=1; s[i]!='\0'; i++){
        if(s[i]==s[i-1]) cur++;
        else{
            cnt+=fmin(cur, prev);
            prev=cur;
            cur=1;
        }
    }
    return cnt+fmin(cur, prev);
}