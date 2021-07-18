class Solution:
    def threeEqualParts(self, arr):
        total_ones = arr.count(1)
        fail_state = [-1,-1]
        leng = len(arr)
        target = total_ones // 3
        if total_ones % 3 != 0:
            return [-1,-1]
        if total_ones == 0:
            return [0,2]
        c1 = c2 = c3 = 0
        counter = 0 
        for i, num in enumerate(arr):
            if num == 1:
                if counter == 0:
                    c1 = i
                elif counter == target:
                    c2 = i
                elif counter == 2*target:
                    c3 = i
                counter +=1
                
        prev_c2 = c2
        prev_c3 = c3
        while c3 < leng and c1 < prev_c2 and c2 < prev_c3:
            if arr[c1] != arr[c2] or arr[c1] != arr[c3]:
                return fail_state
            else:
                c1 +=1
                c2 +=1
                c3 +=1
        return [c1 -1 , c2] if c3 == leng else fail_state


    def oldThreeEqualParts(self, arr):
        get_sum = sum(arr)
        arr_len = len(arr)
        depo = [0]*arr_len
        if get_sum % 3 != 0:
            return [-1,-1]
        else:
            index_finder = get_sum / 3
            sum_in = 0
            set_i = False
            set_j = False
            final_beti = 0
            get_i = 0
            p_count = ""
            q_count = ""
            r_count = ""
            for j, i in enumerate(arr):
                sum_in+=i
                if set_i and final_beti ==0 and sum(arr[get_i+1:j])==index_finder and get_i+1 < j:
                    final_beti = j
                    set_j = True
                    break
                if sum_in > index_finder and not set_i:
                    set_i = True
                    get_i = j - 1 
            print(get_i,j)
            p_count = "".join([str(kk) for kk in arr[0:get_i+1]]).lstrip("0")
            q_count = "".join([str(kk) for kk in arr[get_i+1:j]]).lstrip("0")
            r_count = "".join([str(kk) for kk in arr[j:]]).lstrip("0")
            # print(p_count)
            # print(q_count)0
            # print(r_count)
            return [get_i,final_beti] if p_count == q_count and q_count == r_count else [-1,-1]


if __name__=="__main__":
    kk = Solution()
    ll = kk.threeEqualParts([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0])
    print(ll)
    ll = kk.threeEqualParts([1,0,1,0,1])
    print(ll)

    ll = kk.threeEqualParts([1,0,1,1,0])
    print(ll)