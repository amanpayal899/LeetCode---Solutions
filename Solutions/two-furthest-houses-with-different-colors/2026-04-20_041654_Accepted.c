# Problem: Two Furthest Houses With Different Colors
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9 MB
# Submitted: 2026-04-20_041654 UTC
# URL: https://leetcode.com/submissions/detail/1983188989/

int maxDistance(int* colors, int colorsSize) {
    int maxDistance=0;
    for(int i=0,j=colorsSize-1; j>i; )
    {
        if( colors[i]!=colors[j] )
        {
            if( j-i > maxDistance )
            {
                maxDistance = j-i;  
            }
            i++;
            j=colorsSize-1;
        }
        else j--;
    }
    return maxDistance;
}