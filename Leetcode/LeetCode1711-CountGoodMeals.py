class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # 分組統計
        pows = [2 ** i for i in range(22)]  # 2的0次到2的21次方的清單
        freq_dict = collections.Counter(deliciousness)  # 記錄每個數字出現幾次的字典
        keys = sorted(list(freq_dict.keys()))  # 所有出現過的數字

        ans = 0
        # 對於pows的每一項遍歷
        for po in pows:
            uniq_dict = {}  # 對於當前目標的 2sum 運算
            # 對於freq_dict的所有數字做一遍
            for num in keys:
                # 如果數字沒有出現在uniq_dict 且 跟freq_dict的數字加起來會是2的n次方
                if num not in uniq_dict and po - num in freq_dict:
                    # 如果自己加自己等於2的n次方
                    if po - num == num:
                        ans += freq_dict[num] * \
                            (freq_dict[num] - 1) // 2  # C n 取 2
                    # 兩個數不相同
                    else:
                        ans += freq_dict[num] * \
                            freq_dict[po-num]  # 兩個數字各自出現的次數相乘
                    uniq_dict[num] = 1
                    uniq_dict[po-num] = 1
        return ans % (10**9 + 7)
