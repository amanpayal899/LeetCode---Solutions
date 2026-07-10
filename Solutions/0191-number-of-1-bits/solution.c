int hammingWeight(int n) {
    int c = 0;
    int temp = n;
        while (temp>0){
            c ++;
            temp = (((~temp)+1)^temp)&temp;
        }
        return c;
}
