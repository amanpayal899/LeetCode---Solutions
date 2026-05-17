bool isAdjacentDiffAtMostTwo(char* s) {
    for( int i=0; s[i+1]!='\0'; i++ ){
        if( (s[i] - s[i+1] > 2) || (s[i+1] - s[i] > 2) )
            return false;
    }
    return true;
}
