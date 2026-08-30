# Problem: Furthest Point From Origin
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.4 MB
# Submitted: 2026-04-25_161204 UTC
# URL: https://leetcode.com/submissions/detail/1987907026/

int furthestDistanceFromOrigin(char* moves) {
    int _count=0, leftCount=0, rightCount=0, pos = 0;
    for( int i=0; moves[i]!='\0'; i++ )
    {
        if( moves[i] == 'L' )
        leftCount++;
        else if( moves[i] == 'R' )
        rightCount++;
        else
        _count++;
    }
    if( rightCount >= leftCount )
    pos = rightCount - leftCount + _count;
    else
    pos = leftCount - rightCount + _count;
    return pos;
}