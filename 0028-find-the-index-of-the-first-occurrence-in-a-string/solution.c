int strStr(char* haystack, char* needle) {
    int i=0,j=0,count=0;
    while(haystack[i]!='\0'&& needle[j]!='\0'){
        if(haystack[i]!=needle[j]){
            count++;j=0;i=count;continue;
        } 
        else{
            i++;j++;
        }
    }
    if(needle[j]=='\0') return i-j;
    else return -1;
}
