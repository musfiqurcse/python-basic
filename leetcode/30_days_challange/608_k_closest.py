class Solution:
    def pusher(self, arr: List[int], obj: dict, num: int, main_num: int):
        if not num in arr:
            arr.append(num)
        record_item = obj.get(num, [])
        record_item.append(main_num)
        obj[num] = record_item
        
        
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        # input 1,2,3,4,5,6,7,8,9 x =  5
        # input -1 -2 -3 -4 0 1 2 3 x = 0 
        max_num = arr[-1]
        min_num = arr[0]
        forward_push = True
        if not (abs(x - min_num)  < abs(x - max_num)):
            forward_push = False
        dist = []
        main_dict = {}
        final_list = []
        if forward_push:
            for i in arr:
                self.pusher(dist, main_dict, abs(x - i), i)
        else:
            for i in reversed(arr):
                self.pusher(dist, main_dict, abs(x - i), i)
        dist = sorted(dist)
        #print(dist)
        for i in dist:
            final_list = final_list + sorted(main_dict[i])
            #print(final_list)
            if len(final_list) >= k:
                final_list = final_list[:k]
                break
        return sorted(final_list)