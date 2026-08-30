# Problem: Plus One
# Status: Runtime Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-07_062446 UTC
# URL: https://leetcode.com/submissions/detail/1940505900/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    long large_integer = 0;
    for( int i=0 ; i<digitsSize ; i++){
        large_integer = large_integer * 10 + digits[i];
    }
    large_integer++;
    long temp = large_integer;
    int digits_count=0;
    while( temp > 0 ){
        temp/=10;
        digits_count++;
    }
    *returnSize = digits_count;
    int *arr = (int*)malloc(digits_count*sizeof(int));
    digits_count--;
    while( digits_count >= 0){
        arr[ digits_count--] = large_integer%10;
        large_integer /= 10;
     
    }
    return arr;
   
}