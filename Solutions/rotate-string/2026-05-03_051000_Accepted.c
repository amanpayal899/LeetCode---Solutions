# Problem: Rotate String
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-05-03_051000 UTC
# URL: https://leetcode.com/submissions/detail/1993883362/

bool rotateString(char* s, char* goal) {
    if( strcmp(s, goal) == 0 )
    return true;
    int size = strlen(s);
    char temp[size + 1];
    for( int i=1; s[i]!='\0'; i++)
    {
        if( s[i] == goal[0]){
            for( int j=0; j<size; j++ )
            {
                int idx = (i + j)%size;
                temp[j] = s[idx];
            }
            temp[size] = '\0';
        }
        if( !strcmp(temp, goal) )
        return true;
    }
    return false;
}