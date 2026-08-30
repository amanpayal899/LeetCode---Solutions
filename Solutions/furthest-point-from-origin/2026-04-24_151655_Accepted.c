# Problem: Furthest Point From Origin
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.1 MB
# Submitted: 2026-04-24_151655 UTC
# URL: https://leetcode.com/submissions/detail/1987086016/

int furthestDistanceFromOrigin(char* moves) {
    int rightposition=0, leftposition=0;
    for( int i=0; moves[i]!= '\0'; i++ )
    {
        if( moves[i] == 'L' )
        {
            leftposition--;
            rightposition--;
        }
        else if( moves[i] == 'R' )
        {
            rightposition++;
            leftposition++;
        }
        else
        {
            rightposition ++;
            leftposition --;
        }
    }
    if( rightposition >= (-1 * leftposition ) )
    return rightposition;
    return -1 * leftposition;
}