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
