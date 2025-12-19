import random


def lottery_by_set(numbers):
    # 產生開獎號碼
    buyer_nums = set(numbers)
    lottery_nums = set()
    while len(lottery_nums) < 6:
        lottery_nums.add(random.randint(1, 49))

    bingo_nums = lottery_nums & buyer_nums  # 計算中獎號碼
    return lottery_nums, bingo_nums


def lottery_by_list(numbers):
    # 產生開獎號碼
    buyer_nums = list(numbers)
    lottery_nums = []
    while len(lottery_nums) < 6:
        num = random.randint(1, 49)
        if num not in lottery_nums:
            lottery_nums.append(num)

    # 計算中獎號碼
    bingo_nums = []
    for num1 in lottery_nums:
        for num2 in buyer_nums:
            if num1 == num2:
                bingo_nums.append(num1)
                break
    return lottery_nums, bingo_nums


buyer_nums = (2, 6, 10, 23, 34, 45)  # 買家獎券號碼
# lottery_nums, bingo_nums = lottery_by_set(buyer_nums)
lottery_nums, bingo_nums = lottery_by_list(buyer_nums)
print(f"開獎號碼：{lottery_nums}")
print(f"買家號碼：{buyer_nums}")
print(f"中了 {len(bingo_nums)} 個號碼", bingo_nums)
