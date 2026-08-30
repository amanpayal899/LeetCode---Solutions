# Problem: Detect Capital
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-05-12_185539 UTC
# URL: https://leetcode.com/submissions/detail/2001623835/

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