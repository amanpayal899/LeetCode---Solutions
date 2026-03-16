#include<string.h>
#include<ctype.h>
bool isPalindrome(char* s) {
    char* only_alphabets = (char*)malloc(strlen(s)*sizeof(char)) ;
    int j=0 ;
    for( int i=0 ; s[i]!='\0' ; i++ )
    {
        if( (s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z') || (s[i]>='0' && s[i]<='9'))
        {
            only_alphabets[j++] = tolower(s[i]) ;

        }
    }
    for( int start=0,end=j-1 ; start<=end ; start++,end-- )
    {
        if( only_alphabets[start] != only_alphabets[end] )
        {
            return false ;
        }
        
    }
    return true;

}
