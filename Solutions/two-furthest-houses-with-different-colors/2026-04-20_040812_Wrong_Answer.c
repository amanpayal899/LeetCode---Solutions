# Problem: Two Furthest Houses With Different Colors
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-20_040812 UTC
# URL: https://leetcode.com/submissions/detail/1983182825/

int maxDistance(int* colors, int colorsSize) {
    int maxDistance=0;
    for(int i=0,j=colorsSize-1; j>i; j--)
    {
        if( colors[i]!=colors[j] )
        {
            maxDistance = j-i;
            break;
        }
    }
    return maxDistance;
}