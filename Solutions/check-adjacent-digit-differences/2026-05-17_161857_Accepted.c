# Problem: Check Adjacent Digit Differences
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.6 MB
# Submitted: 2026-05-17_161857 UTC
# URL: https://leetcode.com/submissions/detail/2005695394/

bool isAdjacentDiffAtMostTwo(char* s) {
    for( int i=0; s[i+1]!='\0'; i++ ){
        if( (s[i] - s[i+1] > 2) || (s[i+1] - s[i] > 2) )
            return false;
    }
    return true;
}