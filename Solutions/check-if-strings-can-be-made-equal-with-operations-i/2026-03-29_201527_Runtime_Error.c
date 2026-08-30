# Problem: Check if Strings Can be Made Equal With Operations I
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-29_201527 UTC
# URL: https://leetcode.com/submissions/detail/1963226392/

bool canBeEqual(char* s1, char* s2) {
    for( int i=0,j=0 ; i<4 ; i++ )
    {
        if (s1[i]==s2[i]){
            j++;
            continue;
        }
        if(s1[j]==s2[j+2] && s2[j]==s1[j+2])
        {
            s1[j]=s2[j];
            s1[j+2]=s2[j+2];
            j++;
        }
        
        if(s1[i]!=s2[i]) 
        return false;
    }
    return true;
}