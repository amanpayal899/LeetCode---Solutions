# Problem: Find the Difference
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-15_143506 UTC
# URL: https://leetcode.com/submissions/detail/1885891957/

char findTheDifference(char* s, char* t) {int flag=-1,count=0;
   for(int i=0;t[i]!='\0';i++){
    for(int j=0;s[j]!='\0';j++){
        if(t[i]==s[j]&& j!=flag){
            flag=j;count++;
            break;
        }
    }
    if(count==0) return t[i];
    count=0;
   } 
   return '\0';
}