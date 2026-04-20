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
