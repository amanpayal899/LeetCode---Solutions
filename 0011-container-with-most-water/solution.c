int maxArea(int* height, int heightSize) {
   int small , maxwater=0;
   int i=0 , j= heightSize-1;
   while(i!=j){
    if(height[i] > height[j])
    small = j;
    else small = i;
    if(maxwater<height[small]*(j-i))
    maxwater=height[small]*(j-i);
    if(small==i) i++;
    else j--;

   }
   return maxwater ;
}
