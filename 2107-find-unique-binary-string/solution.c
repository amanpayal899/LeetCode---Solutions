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
