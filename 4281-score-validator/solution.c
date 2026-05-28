/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<string.h>
int* scoreValidator(char** events, int eventsSize, int* returnSize) {
   int *result = (int*)malloc(2*sizeof(int));
    int counter=0, score=0;
    for(int i=0; i<eventsSize && counter<10; i++){
        switch(events[i][0]){
            case '1': score += 1;
                break;
            case '2': score += 2;
                break;
            case '3': score += 3;
                break;
            case '4': score += 4;
                break;
            case '6': score += 6;
                break;
            case 'W': if( events[i][1]=='\0')
                counter += 1;
                break;
        }
        if(!strcmp(events[i], "WD"))
            score += 1;
        else if(!strcmp(events[i], "NB"))
            score += 1;
    }
    result[0] = score;
    result[1] = counter;
    *returnSize = 2;
    return result;
}
