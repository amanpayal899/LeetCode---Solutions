

int fib(int n){
    if(n<=1)
    return n ;
 int *p = malloc( (n+1) * sizeof(int)) ;
 p[0]=0;
 p[1]=1;
 for(int i = 2 ; i<=n ; i++){
    p[i]=p[i-1] + p[i-2];
 }
 n = p[n] ;
 free(p);
 return n;
}
