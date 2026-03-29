bool canBeEqual(char* s1, char* s2) {
    for( int i=0 ; i<2 ; i++ )
    {
        if((s1[i]==s2[i+2] && s2[i]==s1[i+2]))
        {
            s1[i]=s2[i];
            s1[i+2]=s2[i+2];
        }
    }
    for( int i=0 ; i<4 ; i++ )
    {
        if( s1[i]!=s2[i] )
        return false;
    }
    return true;
}
