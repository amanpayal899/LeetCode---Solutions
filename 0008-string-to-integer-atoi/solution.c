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
        if( num>2147483647 )
        {
            if( sign == '+' )
                return 2147483647;
            else if ( sign == '-' )
                return -2147483648;
        }
        i++;
    } 
    if(sign == '-')
    num *= (-1);
    return num;
}
