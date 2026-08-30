# Problem: Length of Last Word
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-24_185802 UTC
# URL: https://leetcode.com/submissions/detail/1895676060/

int lengthOfLastWord(char* s) {
    int count =0;int i=0;
    for(;s[i]!='\0';i++);
    for(;s[i-1]!=' '||count==0;i--){
         if(s[i-1]==' ')
         continue;
         count++;
    }
    return count;
}