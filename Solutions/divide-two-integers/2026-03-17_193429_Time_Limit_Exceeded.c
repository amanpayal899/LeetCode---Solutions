# Problem: Divide Two Integers
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-17_193429 UTC
# URL: https://leetcode.com/submissions/detail/1951488566/

#include<math.h>
int divide(int dividend, int divisor) {
    if( dividend > (pow(2,31)-1))
    return pow(2,31)-1;
    else if( dividend < -(pow(2,31)-1))
    return (-pow(2,31));
    long count=0 ; long sum=0;
    if( dividend < 0 )
    {
        while( sum>dividend )
        {
            sum -= divisor ;
            count--;
        }
        count++;
    }
    else
    {
        while( sum<dividend)
        {
          sum += divisor ;
          count++;
        }
        count--;
    }
    return count;

}