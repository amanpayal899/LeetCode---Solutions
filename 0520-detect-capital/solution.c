bool detectCapitalUse(char* word) {
    int capital_count=0, small_count=0;
    for( int i=0; word[i] != '\0'; i++ ){
        if(word[i] >= 'a' && word[i] <= 'z'){
            if( capital_count >1 )
                return false;
            small_count ++;
        }
        else if( word[i] >= 'A' && word[i] <= 'Z' ){
            if( small_count>0)
                return false;
            capital_count++;
        }
    }
    return true;
}
