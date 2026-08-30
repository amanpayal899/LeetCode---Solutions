# Problem: Minimum Changes To Make Alternating Binary String
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.8 MB
# Submitted: 2026-03-05_074452 UTC
# URL: https://leetcode.com/submissions/detail/1938513605/

int minOperations(char* s) {
    int zero_at_even = 0;
    int zero_at_odd = 0;
    for( int i=0 ; s[i]!='\0' ; i++ ){
       if( i%2 == 0){
        if( s[i] == '0')
          zero_at_odd++;
        else
           zero_at_even++;
       }
       else{
        if(s[i] == '1')
          zero_at_odd++;
        else
          zero_at_even++;
       }
    }
    
    if( zero_at_odd > zero_at_even)
    return zero_at_even;
    return zero_at_odd;
}