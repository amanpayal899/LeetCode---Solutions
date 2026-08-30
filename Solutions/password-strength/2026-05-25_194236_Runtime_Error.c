# Problem: Password Strength
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-05-25_194236 UTC
# URL: https://leetcode.com/submissions/detail/2012978535/

int passwordStrength(char* password) {
    int small_arr[25] = {0};
    int capital_arr[25] = {0};
    int digit_arr[10] = {0};
    int char_arr[4] = {0};
    for(int i=0; password[i]!='\0'; i++){
        if(password[i]>='a' && password[i]<='z'){
            small_arr[password[i]-'a'] = 1;
        }
        else if(password[i]>='A' &&password[i]<='Z'){
            capital_arr[password[i]-'A'] = 2;
        }
        else if(password[i]>='0' && password[i]<='9'){
            digit_arr[password[i]-'0']=3;
        }
        else{
            if( password[i] == '!')
                char_arr[0]=5;
            else if(password[i]=='@')
                char_arr[1] = 5;
            else if(password[i]=='#')
                char_arr[2] = 5;
            else 
                char_arr[3] = 5;
        }
    }
    int points=0;
    for(int i=0,j=0,k=0; i<25; i++){
        if(small_arr[i]==1)
            points += 1;
        if(capital_arr[i]==2)
            points+=2;
        if(j<10 && digit_arr[j++]==3)
            points+=3;
        if(k<4 && char_arr[k++]==5)
            points+=5;
    }
    return points;
}