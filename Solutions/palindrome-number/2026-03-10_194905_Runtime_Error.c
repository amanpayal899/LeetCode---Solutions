# Problem: Palindrome Number
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-10_194905 UTC
# URL: https://leetcode.com/submissions/detail/1944330592/

bool isPalindrome(int x) {
    int rev=0;
    int temp = x;
    while( temp>0 )
    {
        rev = 10*rev + temp%10 ;
        temp = temp/10;
    }
    if ( rev == x )
    return true;
    return false;
}