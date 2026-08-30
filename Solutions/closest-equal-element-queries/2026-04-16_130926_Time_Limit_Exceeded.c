# Problem: Closest Equal Element Queries
# Status: Time Limit Exceeded
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-16_130926 UTC
# URL: https://leetcode.com/submissions/detail/1980062662/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* solveQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    // 1. Allocate memory for the results
    int* result = (int*)malloc(queriesSize * sizeof(int));
    if (result == NULL) {
        *returnSize = 0;
        return NULL;
    }
    
    *returnSize = queriesSize;

    // 2. Process each query
    for (int i = 0; i < queriesSize; i++) {
        int start_idx = queries[i];
        int target_val = nums[start_idx];
        int min_dis = -1;

        // 3. Search the entire nums array for the same value
        for (int j = 0; j < numsSize; j++) {
            // Skip the starting index itself
            if (j == start_idx) continue;

            if (nums[j] == target_val) {
                // Calculate Linear Distance: |start_idx - j|
                int linear_d = (start_idx > j) ? (start_idx - j) : (j - start_idx);
                
                // Calculate Wrap-around Distance: Total - Linear
                int circular_d = numsSize - linear_d;
                
                // The true distance to this specific 'j' is the smaller path
                int current_best_for_j = (linear_d < circular_d) ? linear_d : circular_d;

                // Update the overall minimum distance for this query
                if (min_dis == -1 || current_best_for_j < min_dis) {
                    min_dis = current_best_for_j;
                }
                
                // Optimization: If we found a neighbor (distance 1), 
                // we can't get any closer.
                if (min_dis == 1) break;
            }
        }
        result[i] = min_dis;
    }

    return result;
}