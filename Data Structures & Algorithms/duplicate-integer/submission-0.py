class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        isNumber = set()
        for n in nums:
            if n in isNumber:
                # print("Duplicate found :",n)
                return True
            isNumber.add(n)
        return False
                