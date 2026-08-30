# Problem: Check Adjacent Digit Differences
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-17_161221 UTC
# URL: https://leetcode.com/submissions/detail/2005690152/

bool isAdjacentDiffAtMostTwo(char* s) {
    for( int i=0; s[i+1]!='\0'; i++ ){
        if( (s[i] - s[i+1] > '2') || (s[i+1] - s[i] > 2) )
            return false;
    }
    return true;
}