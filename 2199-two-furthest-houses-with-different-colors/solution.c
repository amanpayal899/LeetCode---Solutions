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
