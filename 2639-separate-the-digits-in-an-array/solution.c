/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 void total_digits(int temp, int *digit_ptr)
 {
    if( temp == 0 )
        return;
    else{
        total_digits(temp/10, digit_ptr);
        (*digit_ptr)++;
    }
 }

 void ans_array(int temp, int *ans_ptr, int *j_ptr){
    if( temp == 0 )
        return;
    else{
        ans_array(temp/10, ans_ptr, j_ptr);
        ans_ptr[(*j_ptr)++] = temp%10;
        return;
    }
 }
int* separateDigits(int* nums, int numsSize, int* returnSize) {
    int digits =0;
    for( int i=0; i<numsSize; i++ )
    {
       total_digits(nums[i], &digits);
    }
    int* ans = (int*)malloc(digits*sizeof(int));
    *returnSize = digits;
    int j = 0;
    for( int i=0; i<numsSize; i++ ){
        
        ans_array(nums[i], ans, &j);
    }
    return ans;
}
