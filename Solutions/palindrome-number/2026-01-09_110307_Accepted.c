# Problem: Palindrome Number
# Status: Accepted
# Language: c
# Runtime: 2 ms
# Memory: 8.1 MB
# Submitted: 2026-01-09_110307 UTC
# URL: https://leetcode.com/submissions/detail/1879684928/

bool isPalindrome(int x) {
    long int rev_num=0;
    long int num=x;
    while(num>0){
        rev_num=10*rev_num+num%10;
        num=num/10;
    }
    if(rev_num==x)
    return true;
    else return false;
}