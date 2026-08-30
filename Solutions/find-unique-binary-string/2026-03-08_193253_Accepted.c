# Problem: Find Unique Binary String
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.9 MB
# Submitted: 2026-03-08_193253 UTC
# URL: https://leetcode.com/submissions/detail/1942242365/

char* findDifferentBinaryString(char** nums, int numsSize) {
   char *str = (char*)malloc((numsSize+1)*sizeof(char)) ;
  int i=0 ;
  for( ; i<numsSize ; i++)
   {
    str[i] = nums[i][i]^1 ;
   }
   str[i]='\0';
   return str;
}