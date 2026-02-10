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
