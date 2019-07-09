# PSEUDOCODE
# MaxSub(a[1, … , n])
# For each pair (i, j) with i <= j 
#      compute a[i]+a[i+1]+· · · +a[j-1]+a[j]
#      Keep the max sum found so far
# Return max sum
import random

running_sum = 0;
max_sum = 0;
array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84];
i = 0;
j = len(array);

for x in range(i, j):
    running_sum += array[x];
    if running_sum < 0:
        running_sum = 0;
    if max_sum < running_sum:
        max_sum = running_sum;
print(max_sum);

    
