def decompressRLElist(nums: list[int]) -> list[int]:
    lst = []
    while nums:
        freq = nums.pop(0)
        if nums:
            val = nums.pop(0)
        else:
            break
        for _ in range(freq):
            lst.append(val)
    return lst


if __name__ == '__main__':
    nums = [1, 1, 2, 3]
    print(decompressRLElist(nums))
