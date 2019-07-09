import random

n = random.randint(2,20);
arr = [];
for i in range(n):
    arr.append(random.randint(-100,100));
    
max_so_far = arr[0];
curr_max = arr[0];

for i in range(1, n):
    curr_max = max(arr[i], curr_max + arr[i]);
    max_so_far = max(max_so_far, curr_max);

print(max_so_far);
print(arr);