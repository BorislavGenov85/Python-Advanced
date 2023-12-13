def sum_nums(*nums):
    sum_negative = 0
    sum_positive = 0

    for num in nums:
        if num < 0:
            sum_negative += num
        else:
            sum_positive += num

    if abs(sum_negative) > abs(sum_positive):
        return f"{sum_negative}\n{sum_positive}\nThe negatives are stronger than the positives"
    return f"{sum_negative}\n{sum_positive}\nThe positives are stronger than the negatives"


data = [int(x) for x in input().split()]
print(sum_nums(*data))
