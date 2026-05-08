int sumOfPrimesInRange(int n) {
  int temp = n;
  int rev=0;
    while( temp > 0 )
    {
        rev = rev*10 + temp%10;
        temp = temp / 10;
    }
    int start = ( n>rev ? rev : n);
    int end = ( n>rev ? n : rev );
    int flag = 1;
    int prime_sum = 0;
    for( int i=start; i<=end; i++)
    {
        flag = 1;
        if( i==1 )
            continue;
        for( int j=2; j<=i/2; j++)
        {
            if( i%j == 0 )
            {
                flag = 0;
                break;
            }
        }
        if( flag == 1 )
        {
             prime_sum += i;
        }
    }
    return prime_sum;
}
