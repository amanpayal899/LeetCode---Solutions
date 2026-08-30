# Problem: Sqrt(x)
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.5 MB
# Submitted: 2026-02-10_160740 UTC
# URL: https://leetcode.com/submissions/detail/1914843587/

int mySqrt(int x) {
    long mid ; int ans;int start=0 , end = x ;
    while( start<=end){
       mid = (start + end)/2 ;
        if( mid*mid <= x ){
            start = mid+1 ;
            ans=mid;
        }
        else
        {
            end = mid-1 ;
        }
    }
    return ans;
}