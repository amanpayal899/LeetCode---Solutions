bool judgeCircle(char* moves) {
    int u=0,r=0;
    for( int i=0; moves[i]!='\0'; i++ )
    {
        if( moves[i] == 'U')
        u++;
        else if(moves[i] == 'D')
        u--;
        else if(moves[i] == 'R')
        r++;
        else if(moves[i] == 'L')
        r--;
    }
    return (u==0 && r==0);
}

