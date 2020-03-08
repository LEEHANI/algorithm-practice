#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    a=-1
    count=1
    answer=0

    for i in ar:
        if i == a:
            count+=1
        else:
            answer += count//2
            a=i 
            count=1
    answer += count//2
    return answer

# print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))
print(sockMerchant(10, [1,1,3,1 ,2 ,1 ,3 ,3 ,3, 3]))