def math_operations(*nums, **kwargs):
    for i in range(len(nums)):
        key = list(kwargs.keys())[i % 4]

        if key == "a":
            kwargs[key] += nums[i]
        elif key == "s":
            kwargs[key] -= nums[i]
        elif key == "d":
            if nums[i] != 0:
                kwargs[key] /= nums[i]
        elif key == "m":
            kwargs[key] *= nums[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{key}: {value:.1f}" for key, value in kwargs)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-
2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
