# Problem: String to Integer (atoi)
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-04_073407 UTC
# URL: https://leetcode.com/submissions/detail/1968380040/

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
    else if (s[i] == '+')
        i++;
    while( s[i]=='0')
    {
        i++;
    }
    while( s[i]!='\0' && (s[i]>='0' && s[i]<='9') )
    {
        num = 10*num+(s[i]-'0');
        if( num>2147483647 && sign =='-' )
        return -2147483648;
        i++;
    }
    if(sign == '-')
    num *= (-1);
    if( num > 2147483647 )
    return 2147483647;
    return num;
}