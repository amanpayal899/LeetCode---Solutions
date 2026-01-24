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
