# Problem: Length of Last Word
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8 MB
# Submitted: 2026-01-24_192639 UTC
# URL: https://leetcode.com/submissions/detail/1895698048/

int lengthOfLastWord(char* s) {
    int count =0;int i=0;
    for(;s[i]!='\0';i++);
    i--;
    for(;i>=0&&(s[i]!=' '||count==0);i--){
        if(s[i]==' ') continue;
        count++;
    }
    return count;
}