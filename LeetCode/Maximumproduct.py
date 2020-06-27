def maxProduct(nums):
    working = sorted(nums)
    c = 0
    highest = [working[-1], working[-2]]
    solutions = []
        
    while c <= len(nums)-1:
        if nums[c] in highest:
            solutions.append(nums[c])

        c = c + 1

    final = 1
    for i in solutions:
        final = final * (i-1)

    print(final)

list = [3,4,5,2]
maxProduct(list)
