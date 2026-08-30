# Problem: Smallest Stable Index II
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-21_180544 UTC
# URL: https://leetcode.com/submissions/detail/1984718106/

int firstStableIndex(int* nums, int numsSize, int k) {
  int max=nums[0], min=nums[0];
    for( int i=0,j=0; i<numsSize; )
    {
        if( j<i )
        {
            if( nums[j] > max )
            {
                max = nums[j];
                
            }
            j++;
        }
        else if( j>=i && j!=numsSize-1)
        {
            if( min > nums[j+1] )
            {
                min = nums[j+1];
                
            }
            j++;
        }
        else if( j == numsSize-1 )
        {
            if( max - min <= k )
                return i;
            i++;
            if( i!= numsSize )
            {
                max=nums[0];
                min=nums[i];
            }
                
            j=0;
            
        }
    }
    return -1;
}