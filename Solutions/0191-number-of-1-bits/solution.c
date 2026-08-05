int hammingWeight(int n) {
    int cpy = n;
    int count = 0;
    while( cpy>0){
        cpy = cpy & (cpy-1);
        count ++;
    }
    return count;
}
