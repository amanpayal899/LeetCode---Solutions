# Problem: String to Integer (atoi)
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-03_183505 UTC
# URL: https://leetcode.com/submissions/detail/1968011190/

int myAtoi(char* s) {
    int i=0;
    long num=0;
    char sign='+';
    while(s[i]==' ')
    {
        i++;
    }
    if( s[i]=='-' )
    {
         sign='-';
         i++;
    }
    while( s[i]=='0')
    {
        i++;
    }
    while( s[i]!='\0' && (s[i]>='0' && s[i]<='9') )
    {

        num = 10*num+(s[i]-'0');
        i++;
    }
    if(sign == '-')
    num *= (-1);
    return num;
}