int countBinarySubstrings(char* s) {
   int result=1,num=0;
    for( int i=0 ; s[i+1]!='\0' ; i++){
        if(s[i] != s[i+1])
        result++;
    }
    
    int arr[result];
    for( int k=0,j=0,count=1; s[j]!='\0' ; j++){
       if(s[j+1] == s[j]){
        count++;continue;
       }
       arr[k++] = count;
       count = 1;
    }
    for(int t=0 ; t<result-1 ; t++){
       if(arr[t]<=arr[t+1])
       num+=arr[t];
       else num+=arr[t+1];
    }
    return num;
}
