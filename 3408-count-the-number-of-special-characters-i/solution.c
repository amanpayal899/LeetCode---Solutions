int numberOfSpecialChars(char* word) {
    int count = 0;
    int *capital_freq = (int*)calloc(26, sizeof(int));
    int *small_freq = (int*)calloc(26, sizeof(int));
    for( int i=0; word[i]!='\0'; i++ ){
        if(word[i]>='a' && word[i]<='z'){
            small_freq[word[i] - 'a'] = 1;
        }
        else if(word[i]>='A' && word[i]<='Z'){
            capital_freq[word[i]-'A'] = 1;
        }
    }
    for(int j=0; j<26; j++){
        if( capital_freq[j] + small_freq[j] == 2)
            count+=1;
    }
    return count;
}
