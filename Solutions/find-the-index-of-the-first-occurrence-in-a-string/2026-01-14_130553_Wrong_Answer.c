# Problem: Find the Index of the First Occurrence in a String
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-14_130553 UTC
# URL: https://leetcode.com/submissions/detail/1884816987/

int strStr(char* haystack, char* needle) {
    int i=0,j=0;
    while(haystack[i]!='\0'&& needle[j]!='\0'){
        if(haystack[i]!=needle[j]){
            i++;j=0;
        } 
        else{
            i++;j++;
        }
    }
    if(needle[j]=='\0') return i-j;
    else return -1;
}