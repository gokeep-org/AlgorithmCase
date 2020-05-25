def erfen(numbers, target):
    low = 0
    hig = len(numbers) - 1
    if (target < numbers[0]) or (target > numbers[hig]):
        return -1
    while low <= hig:
        index = int((hig + low) / 2)
        print(str(index) + "  " + str(low) + "  " + str(hig))
        if numbers[index] == target:
            return index
        if numbers[index] > target:
            hig = index - 1
        else:
            low = index + 1


if __name__ == '__main__':
    numbers = [1, 3, 4, 6, 9, 11, 12]
    target_index = erfen(numbers, 3)
    print(target_index)

    # print(int(9/2))

# 允许高位 > 低位
# index = 取中位数
# if 中间数 = 目标数：return 中间数索引位置
# if 中间数 > 目标数：index = 高位 - 1 (去掉当前数并且防止两个数死循环)
# if 中间数 < 目标数：index = 低位 + 1
