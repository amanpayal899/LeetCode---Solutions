# Problem: Trionic Array I
# Status: Compile Error
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-02-04_190442 UTC
# URL: https://leetcode.com/submissions/detail/1908361330/

bool isTrionic(int* nums, int numsSize) {
    bool isTrionic(int* nums, int numsSize) {
    int p = 0;
    int n_1 = numsSize - 1;

    while(p < n_1 && nums[p] < nums[p+1]){
        p += 1;
    }

    int q = p;
    while(q < n_1 && nums[q] > nums[q+1]){
        q += 1;
    }

    int r = q;
    while(r < n_1 && nums[r] < nums[r+1]){
        r += 1;
    }

    return (p>0) && (p < q) && (q < n_1) && (r==n_1);
}
}