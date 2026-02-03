bool isTrionic(int* nums, int numsSize) {
    int count = 0 ;int i =0 , j=0 ;
    for( ; i<numsSize-1 ; i++){

        if(nums[i] == nums[i+1])
        return false ;

        else if(nums[i] < nums[i+1]){
             if(count ==3 || count ==0)
             count+=2;
            }
        else if ( (nums[i+1] <nums[i])){
            if(i==0) break;
            if(count == 2 || count == 5 ){
            count ++;
            }
        }
        
    }
    if(count == 5)
    return true ;
    return NULL ;
}
