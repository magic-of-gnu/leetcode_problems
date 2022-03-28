from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        def pop_keys(sorted_keys, counter):
            for key in sorted_keys:  # 1,2,3,6
                if key not in counter:
                    continue

                count = counter.pop(key)

                if key+key not in counter:
                    return False
                elif counter[key+key] < count:
                    return False

                counter[key+key] -= count
                if counter[key+key] == 0:
                    counter.pop(key+key)
                    
            return None
        
        counter = dict()
        pos_values, neg_values = set(), set()
        
        for num in arr:
            counter[num] = counter.get(num,0) + 1
            
            if num > 0:
                pos_values.add(num)
            elif num < 0:
                neg_values.add(num)
        
        
        if 0 in counter and counter[0] % 2 != 0:
            return False
        
        if 0 in counter:
            counter.pop(0)
        
        sorted_pos = list(sorted(pos_values))
        sorted_neg = list(reversed(sorted(neg_values)))
        
        sorted_keys = sorted_pos
        
        res = pop_keys(sorted_pos, counter)
        if res is False:
            return False
        
        res = pop_keys(sorted_neg, counter)
        if res is False:
            return False
        
        return True if not counter else False

    from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        counter = Counter(arr)

        if 0 in counter and counter[0] % 2 != 0:
            return False

        if 0 in counter:
            counter.pop(0)

        nums = list(counter.keys())

        for num in nums:

            if num not in counter:
                continue

            num1 = num

            while num1//2 in counter and num1 % 2 == 0:
                num1 = int(num1/2)

            while num1 in counter:

                count = counter.pop(num1)
                num2 = num1 + num1
                if num2 not in counter or counter[num2] < count:
                      return False

                counter[num2] -= count
                if counter[num2] == 0:
                    counter.pop(num2)

                num1 = num2

        return True if not counter else False
