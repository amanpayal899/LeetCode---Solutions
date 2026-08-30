# Problem: Sqrt(x)
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.8 MB
# Submitted: 2026-02-10_160606 UTC
# URL: https://leetcode.com/submissions/detail/1914841740/

int mySqrt(int x) {
    long mid ; int ans;
    for(int start=0 , end = x ; start<=end ;  ){
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