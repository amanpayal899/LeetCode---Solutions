# Problem: Find the Difference
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-15_142519 UTC
# URL: https://leetcode.com/submissions/detail/1885882563/

char findTheDifference(char* s, char* t) {int flag=0;
   for(int i=0;t[i]!='\0';i++){
    for(int j=0;s[j]!='\0';j++){
        if(t[i]==s[j]){
            flag++;
            break;
        }
    }
    if(flag==0) return t[i];
    flag=0;
   } 
   return '\0';
}