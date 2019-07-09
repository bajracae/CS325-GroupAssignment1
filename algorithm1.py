# PSEUDOCODE
# MaxSub(a[1, … , n])
# For each pair (i, j) with i <= j 
#      compute a[i]+a[i+1]+· · · +a[j-1]+a[j]
#      Keep the max sum found so far
# Return max sum

max_sum = 0;
array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84];
i = 0;
j = len(array);

for x in range(i, j):
    max_sum += array[x];

print(max_sum);

    
