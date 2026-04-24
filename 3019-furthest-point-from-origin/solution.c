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
