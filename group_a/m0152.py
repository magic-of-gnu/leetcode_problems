class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        
        def get_max_product(prefix_prod, ii, ii_min, ii_max, n_min, n_max, result):
            
            if ii_min == len(prefix_prod) and ii_max == len(prefix_prod):
                return result
            
            if n_min is None and n_max is None: # if no negative value in the range
                # print('here0')
                return max([result, prefix_prod[ii]])
            elif ii == ii_min and ii == ii_max:
                # print('here1')
                return result
            elif prefix_prod[ii] > 0:
                # print('here2')
                return max([result, prefix_prod[ii]])
            else:
                # print('here3')
                return max([result, prefix_prod[ii]/prefix_prod[n_min], prefix_prod[n_max-1]])
        
        n = len(nums)
        n_min, n_max = None, None
        ii_min, ii_max = 0, 0
        result = nums[0]
        prefix_prod = [0] * (n)
        prod = 1
        
        for ii, x in enumerate(nums):
            
            if x == 0:
                prefix_prod[ii] = 0
                print()
                print(f'ii: {ii} ii_min: {ii_min} ii_max: {ii_max} n_min: {n_min} n_max: {n_max} result: {result}')
                print(prefix_prod)

                result = get_max_product(prefix_prod, ii-1, ii_min, ii_max, n_min, n_max, result)
                
                prod = 1
                n_min, n_max = None, None
                ii_min, ii_max = ii + 1, ii + 1
            else:
                if x < 0:
                    n_min = min([n_min, ii]) if n_min is not None else ii
                    n_max = max([n_max, ii]) if n_max is not None else ii
                    
                ii_min = min(ii, ii_min)
                ii_max = max(ii, ii_max)
                    
                prod *= x
                prefix_prod[ii] = prod
                
        print()
        print(f'ii: {ii} ii_min: {ii_min} ii_max: {ii_max} n_min: {n_min} n_max: {n_max} result: {result}')
        print(prefix_prod)
                
        if x != 0:
            result = get_max_product(prefix_prod, ii, ii_min, ii_max, n_min, n_max, result)
        
        if n_min != 0:
            result = max([0, result])
            
        return int(result)
            
                
        
if __name__ == "__main__":
    nums = [-1, -1, 0]
    Output = 0

    nums = [0,0,0,1,1,-2,10,10,-10,-10,0,-10,-10]
    Output = 10000

    sol = Solution()
    print(sol.maxProduct(nums))

