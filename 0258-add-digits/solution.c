int fun(int num){
        if( num/10 == 0 )
            return num%10;
        else{
            return num%10 + fun( num/10 );
        }
    }
int addDigits(int num) {
    
     while( num/10 != 0){
        int sum = fun(num);
        num = sum;
    }
    return num;
}
