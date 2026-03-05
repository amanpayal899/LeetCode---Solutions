int minOperations(char* s) {
    int p1 = 0;int i=0;
    for(  ; s[i]!='\0' ; i++ ){
        if( i%2 == 0 && s[i] != '0'){
           p1++;
        }
        else if( i%2 == 1 && s[i] != '1')
           p1++;
    }
    if( p1<i-p1)
    return p1;
    return i-p1;
}
