# PSEUDOCODE
# MaxSub(a[1, … , n])
# For each pair (i, j) with i <= j 
#      compute a[i]+a[i+1]+· · · +a[j-1]+a[j]
#      Keep the max sum found so far
# Return max sum
import random

n = random.randint(2, 20)

running_sum = 0;
max_sum = 0;
array = []

for i in range(n):
    array.append(random.randint(-100,100))

for j in range(0, len(array)):
    running_sum += array[j];
    if running_sum < 0:
        running_sum = 0;
    if max_sum < running_sum:
        max_sum = running_sum;
print(max_sum);
print(array)
    
