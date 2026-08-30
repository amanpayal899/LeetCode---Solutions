# Problem: Number of 1 Bits
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.9 MB
# Submitted: 2026-07-10_211200 UTC
# URL: https://leetcode.com/submissions/detail/2063310674/

int hammingWeight(int n) {
    int c = 0;
    int temp = n;
        while (temp>0){
            c ++;
            temp = (((~temp)+1)^temp)&temp;
        }
        return c;
}