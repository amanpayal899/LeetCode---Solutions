# Problem: Count Negative Numbers in a Sorted Matrix
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 9.7 MB
# Submitted: 2026-01-16_153845 UTC
# URL: https://leetcode.com/submissions/detail/1886935444/

int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int count=0;int sizec=*gridColSize , sizer=gridSize;
    for(int r=0;r<sizer;r++){
        for(int c=0;c<sizec;c++){
            if(grid[r][c]<0){
                count=count+(sizec-c);
                break;
            }
        }
    }
    return  count;
}