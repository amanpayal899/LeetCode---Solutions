# Problem: Robot Return to Origin
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9 MB
# Submitted: 2026-04-05_173534 UTC
# URL: https://leetcode.com/submissions/detail/1969861417/

bool judgeCircle(char* moves) {
    int u=0, d=0, r=0, l=0;
    for( int i=0; moves[i]!='\0'; i++ )
    {
        if( moves[i] == 'U')
        u++;
        else if(moves[i] == 'D')
        d++;
        else if(moves[i] == 'R')
        r++;
        else if(moves[i] == 'L')
        l++;
    }
    if( u==d && r==l)
    return true;
    return false;
}
