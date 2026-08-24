class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      dict_new = Counter(nums)

      top_freq = sorted(dict_new.items(),key = lambda x : x[1])
      result = [x[0] for x in top_freq[-k:]]

      return result 
      #{1:1,2:2,3:3}

