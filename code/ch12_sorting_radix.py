# Radix Sort Implementation (Simplified Version)
# Designed for readability and educational purposes.


def radix_sort(arr):
    """
    簡化版的基數排序 (Radix Sort)。
    使用「水桶 (Buckets)」的概念代替複雜的計數排序 (Counting Sort) 邏輯，
    更適合初學者理解。
    """
    # 如果陣列為空或只有一個元素，則已經排序完成
    if len(arr) <= 1:
        return arr

    # 步驟 1: 找出最大值，決定需要排序多少個位數
    max_num = max(arr)

    # exp (exponent) 代表目前的位數。1 代表個位數，10 代表十位數，以此類推。
    exp = 1

    while max_num // exp > 0:
        # 步驟 2: 建立 10 個「水桶」(陣列)，分別代表數字 0 到 9
        buckets = [[] for _ in range(10)]

        # 步驟 3: 將每個數字依據當前的位數，放入對應的水桶中
        for num in arr:
            # 取出當前的位數 (例如 256 的十位數：(256 // 10) % 10 = 5)
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # 步驟 4: 將水桶裡的數字依序取出，重新組合回原陣列
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        # 移至下一個更高的位數 (乘以 10)
        exp *= 10

    return arr


if __name__ == "__main__":
    unsorted_list = [170, 45, 75, 90, 802, 24, 2, 66]
    print("原始列表 (Original List):")
    print(unsorted_list)
    print("-" * 30)

    sorted_list = radix_sort(unsorted_list)
    print("排序後列表 (Sorted List):")
    print(sorted_list)
