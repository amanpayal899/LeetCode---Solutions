# Problem: Detect Capital
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-12_185448 UTC
# URL: https://leetcode.com/submissions/detail/2001623295/

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
        }
    }
    return true;
}