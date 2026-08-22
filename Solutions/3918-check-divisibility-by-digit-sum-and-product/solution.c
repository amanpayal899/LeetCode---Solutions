bool checkDivisibility(int n) {
    // ans = ! ( n % ( digit_sum + product_sum ))
    int digit_sum(int n){
        if (n==0)
            return 0;
        return ( n%10 + digit_sum(n/10));
    }

    int product_sum(int n){
        if (n/10 == 0)
            return n%10;
        return (n%10) * product_sum(n/10);
    }

    return !( n % ( product_sum(n) + digit_sum(n) ));
}

