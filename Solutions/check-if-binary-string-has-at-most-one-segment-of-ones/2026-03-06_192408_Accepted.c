# Problem: Check if Binary String Has at Most One Segment of Ones
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-03-06_192408 UTC
# URL: https://leetcode.com/submissions/detail/1940199337/

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