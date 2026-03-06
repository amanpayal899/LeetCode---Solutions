bool checkOnesSegment(char* s) {
    int count=0;
    for( int i=0 ; s[i+1]!='\0' ; i++){
        if ( s[i] != s[i+1])
           count++;
    }
    if(count == 0 || count ==1)
      return 1;
    return 0;
}
