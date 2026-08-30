# Problem: Surface Area of 3D Shapes
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-14_173629 UTC
# URL: https://leetcode.com/submissions/detail/1948255862/

int surfaceArea(int** grid, int gridSize, int* gridColSize) {
   int sum=0;
   for( int i=0 ; i<gridSize ; i++ )
   {
    for( int j=0 ; j<gridSize ; j++ )
    {
        sum += (grid[i][j] * grid[i][j] * grid[i][j]) ;
    }
   } 
   return sum;
}