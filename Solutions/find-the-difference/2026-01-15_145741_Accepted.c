# Problem: Find the Difference
# Status: Accepted
# Language: c
# Runtime: 15 ms
# Memory: 8.1 MB
# Submitted: 2026-01-15_145741 UTC
# URL: https://leetcode.com/submissions/detail/1885912851/

char findTheDifference(char* s, char* t) {int i=0;
    while(s[i]!='\0'){
        for(int j=0;;j++){
            if(s[i]==t[j]){
                t[j]=0;break;
            }
        }
        i++;
    }
    for(i=0;;i++){
        if(t[i]!=0) return t[i]; 
    }
}