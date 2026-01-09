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
