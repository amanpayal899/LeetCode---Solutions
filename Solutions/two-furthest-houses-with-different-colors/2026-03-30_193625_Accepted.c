# Problem: Two Furthest Houses With Different Colors
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9 MB
# Submitted: 2026-03-30_193625 UTC
# URL: https://leetcode.com/submissions/detail/1964221966/

int maxDistance(int* colors, int colorsSize) {
    int max_dis=0;
    for( int i=0; i<colorsSize; i++ )
    {
        for( int j=colorsSize-1; j>i ; j-- )
        {
            if(( colors[i]!=colors[j] ) && (j-i >= max_dis))
            {
                max_dis=j-i;
                break;
            }
        }
    }
    return max_dis;
}