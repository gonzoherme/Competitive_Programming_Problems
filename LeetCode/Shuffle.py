class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xs = []
        ys = []
        
        counter = 0
        while counter <= len(nums)-1:
            if counter < n:
                xs.append(nums[counter])
            else:
                ys.append(nums[counter])
        
            counter = counter + 1
                
        final = []
        
        c = 0

        
        while c < n:
            final.append(xs[c])
            final.append(ys[c])
            
            c = c + 1
            
        return final
