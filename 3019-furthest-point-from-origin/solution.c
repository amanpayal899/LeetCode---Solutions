int furthestDistanceFromOrigin(char* moves) {
    int _count=0, leftCount=0, rightCount=0;
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
        return rightCount - leftCount + _count;
    else
        return leftCount - rightCount + _count;
}
