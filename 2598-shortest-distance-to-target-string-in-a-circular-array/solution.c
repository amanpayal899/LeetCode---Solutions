#include<string.h>
int closestTarget(char** words, int wordsSize, char* target, int startIndex) {
    int minDistance=-1;
    for(int i=startIndex,j=0; j<wordsSize; i=(i+1)%wordsSize,j++){
        if(!strcmp(words[i],target)){
            if(i>=startIndex)
            minDistance=i-startIndex;
            else
            minDistance=wordsSize-startIndex+i;
            break;
        }
    }
    for(int i=startIndex, j=0; j<wordsSize; i=(i-1+wordsSize)%wordsSize, j++){
        if(!strcmp(words[i],target)){
            if(i>startIndex && minDistance>startIndex+wordsSize-i){
                minDistance=startIndex+wordsSize-i;
                break;
            }
            else if( startIndex>i && minDistance>startIndex-i)
            minDistance=startIndex-i;
        }
    }
    return minDistance;
}
