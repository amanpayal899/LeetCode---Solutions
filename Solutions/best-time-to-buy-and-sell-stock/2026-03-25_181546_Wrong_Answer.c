# Problem: Best Time to Buy and Sell Stock
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-25_181546 UTC
# URL: https://leetcode.com/submissions/detail/1959195062/

int maxProfit(int* prices, int pricesSize) {
    int profit = 0,low = prices[0], high=prices[0],k=0;

    for ( int i=0 ; i<pricesSize-1 ; i++ )
    {
        if( low>=prices[i]){
          low = prices[i];
          high = prices[i];
          k=i;
          }
    }
    
    for( int j=k;j<pricesSize ; j++)
    {
        if( high <= prices[j])
        high = prices[j];
    }
    profit = high - low;
    if (profit == 0)
       return 0;
    return profit;

}