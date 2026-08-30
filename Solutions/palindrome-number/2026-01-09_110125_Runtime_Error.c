# Problem: Palindrome Number
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-01-09_110125 UTC
# URL: https://leetcode.com/submissions/detail/1879683713/

bool isPalindrome(int x) {
    int rev_num=0;
    int num=x;
    while(num>0){
        rev_num=10*rev_num+num%10;
        num=num/10;
    }
    if(rev_num==x)
    return true;
    else return false;
}