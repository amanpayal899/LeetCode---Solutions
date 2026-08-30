# Problem: Best Time to Buy and Sell Stock
# Status: Accepted
# Language: c
# Runtime: 3 ms
# Memory: 15.9 MB
# Submitted: 2026-03-26_203122 UTC
# URL: https://leetcode.com/submissions/detail/1960338519/

int maxProfit(int* prices, int pricesSize) {
    if( pricesSize <= 1 )
      return 0;
    int max_profit=0, min_price=prices[0];
    for( int i=0 ; i<pricesSize ; i++ )
    {
        if( prices[i]< min_price )
        {
            min_price = prices[i];
        }
        else if( (prices[i]-min_price)>max_profit )
        {
            max_profit = prices[i]-min_price;
        }
    }
    return max_profit;
}