import random

arr = [22, -27, 38, -34, 49, 40, 13, -44, -13, 28, 46, 7, -26, 42, 29, 0, -6, 35, 23, -37, 10, 12, -2, 18, -12, -49, -10, 37, -5, 17, 6, -11, -22, -17, -50, -40, 44, 14, -41, 19, -15, 45, -23, 48, -1, -39, -46, 15, 3, -32, -29, -48, -19, 27, -33, -8, 11, 21, -43, 24, 5, 34, -36, -9, 16, -31, -7, -24, -47, -14, -16, -18, 39, -30, 33, -45, -38, 41, -3, 4, -25, 20, -35, 32, 26, 47, 2, -4, 8, 9, 31, -28, 36, 1, -21, 30, 43, 25, -20, -42]
n = len(arr)

#this will generate a random array
#n = random.randint(2,20);
#arr = [];
#for i in range(n):
#    arr.append(random.randint(-100,100));
    
max_so_far = arr[0];
curr_max = arr[0];

for i in range(1, n):
    curr_max = max(arr[i], curr_max + arr[i]);
    max_so_far = max(max_so_far, curr_max);

print(max_so_far);
print(arr);