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
