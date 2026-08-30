# Problem: Check if Strings Can be Made Equal With Operations I
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-29_191736 UTC
# URL: https://leetcode.com/submissions/detail/1963190604/

bool canBeEqual(char* s1, char* s2) {
    
    for( int i=0 ; i<2 ; i++ )
    {
        if( s1[i]==s2[i] )
        continue;
        if ( (s1[i]==s2[i+2] && s2[i]==s1[i+2]) || (s2[i]==s1[i+2] && s1[i]==s2[i+2]) )
        continue;
        else return false;
    }
    return true;
}