# Problem: Shortest Distance to Target String in a Circular Array
# Status: Wrong Answer
# Language: c
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-15_102059 UTC
# URL: https://leetcode.com/submissions/detail/1979079882/

#include<string.h>
int closestTarget(char** words, int wordsSize, char* target, int startIndex) {
    int minDistance=-1;
    for(int i=startIndex,j=0; j<wordsSize; i=(i+1)%wordsSize,j++){
        if(!strcmp(words[i],target)){
            if(i>startIndex)
            minDistance=i-startIndex;
            else
            minDistance=startIndex-i;
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