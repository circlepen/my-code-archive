class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {"}": "{", ")": "(", "]": "["}
        arr = []
        for i in s:
            if i in "[{(":
                arr.append(i)
            else:
                if len(arr) == 0:
                    return False

                if pair_dict[i] == arr[-1]:
                    arr.pop()

                else:
                    return False
        if arr:
            return False
        return True
