class Solution:
    def max_profit(self, prices: list[int]) -> int:
        buy_index, sell_index, max_profit = 0, 1, 0
        while sell_index < len(prices):
            if prices[buy_index] < prices[sell_index]:
                current_profit = prices[sell_index] - prices[buy_index]
                max_profit = max(max_profit, current_profit)
            else:
                buy_index = sell_index
            sell_index += 1
        return max_profit


if __name__ == '__main__':
    s = Solution()
    price_list = [7, 2, 5, 3, 6, 4, 1, 20]
    print(s.max_profit(price_list))
