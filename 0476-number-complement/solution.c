int findComplement(int num) {
    int cpy_num = num ;
    int mask = 1 ;
    if( num == 0)
      return 1;
    while ( cpy_num > 1)
    {
        cpy_num = cpy_num >> 1 ;
        mask = mask << 1 ;
        mask++ ;
    }
    return num^mask ;
}
