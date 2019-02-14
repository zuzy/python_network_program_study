#include <stdlib.h>
#include <string.h>

int maxSubArray(int* nums, int numsSize) {
    int *tmp = (int*)calloc(numsSize, sizeof(int));
    int *p = tmp;
    int i = 0;
    int flag = (nums[i] > 0);
    int sum = nums[i];
    for(i = 1; i < numsSize; i++) {
        if(flag == (nums[i] > 0)) {
            sum += nums[i];
        } else {
            flag = (nums[i] > 0);
            *p++ = sum;
            sum = nums[i];
        }
    }
    --p;
    if(*p < 0) {
        *p = 0;
        --p;
    }
    
    while(p > tmp) {
        
    }
    return 0;
}