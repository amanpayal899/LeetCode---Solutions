# Problem: Check Divisibility by Digit Sum and Product
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.4 MB
# Submitted: 2026-08-22_184921 UTC
# URL: https://leetcode.com/submissions/detail/2116533398/

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
