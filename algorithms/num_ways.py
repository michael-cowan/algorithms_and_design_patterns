

def num_ways(N, x=[1, 2]):
    x = [z for z in x if z <= N]
    if N in [0, 1]:
        return 1
    nums = [None] * (N + 1)
    nums[0] = 1
    for i in range(1, N + 1):
        nums[i] = sum([nums[i - k] for k in x if k < i + 1])
    return nums[N]


print(num_ways(10, x=[1, 3, 5]))
