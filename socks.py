
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n):
    for j in range(n):
        print(" "*(n-j)+"#"*(j+1))
    
if __name__ == '__main__':
    n = int(input())
    sockMerchant(n)
    
   

