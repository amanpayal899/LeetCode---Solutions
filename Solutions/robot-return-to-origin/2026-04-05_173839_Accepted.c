# Problem: Robot Return to Origin
# Status: Accepted
# Language: c
# Runtime: 3 ms
# Memory: 8.9 MB
# Submitted: 2026-04-05_173839 UTC
# URL: https://leetcode.com/submissions/detail/1969864507/

bool judgeCircle(char* moves) {
    int u=0,r=0;
    for( int i=0; moves[i]!='\0'; i++ )
    {
        if( moves[i] == 'U')
        u++;
        else if(moves[i] == 'D')
        u--;
        else if(moves[i] == 'R')
        r++;
        else if(moves[i] == 'L')
        r--;
    }
    if(u==0 && r==0)
    return true;
    return false;
}
