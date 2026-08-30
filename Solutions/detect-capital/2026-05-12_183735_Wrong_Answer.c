# Problem: Detect Capital
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-12_183735 UTC
# URL: https://leetcode.com/submissions/detail/2001611321/

bool detectCapitalUse(char* word) {
   
    int small_count=1, capital_count=1, len=1;
    for( int i=1; word[i] != '\0'; i++ ){
        if( word[i] >= 'A' && word[i] <= 'Z' ){
            capital_count++;
        }
        else{
            small_count++;
        }
        len++;
    }
    if( capital_count == len || small_count == len )
        return true;
    return false;
}