# Problem: Check if Strings Can be Made Equal With Operations I
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.8 MB
# Submitted: 2026-03-29_205853 UTC
# URL: https://leetcode.com/submissions/detail/1963247543/

bool canBeEqual(char* s1, char* s2) {
    for( int i=0 ; i<2 ; i++ )
    {
        if((s1[i]==s2[i+2] && s2[i]==s1[i+2]))
        {
            s1[i]=s2[i];
            s1[i+2]=s2[i+2];
        }
    }
    for( int i=0 ; i<4 ; i++ )
    {
        if( s1[i]!=s2[i] )
        return false;
    }
    return true;
}