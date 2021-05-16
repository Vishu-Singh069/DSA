class Arrays:

    def maximum_sum(self, array_len, k, arr):
        maximum = 0
        temp = 0
        for j in range(0, array_len):
            if (j+k) < array_len:
                for i in range(j, j+k):
                    temp += arr[i]
            else:
                pass
            if temp > maximum:
                maximum = temp
            temp = 0
        return maximum

    def find_sum(self, array_len, result, arr):
        curr_sum = 0
        sub_index = 0
        for index in range(0, array_len):
            curr_sum += arr[index]
            while curr_sum > result:
                curr_sum = curr_sum - arr[sub_index]
                sub_index += 1
            if curr_sum == result:
                return True
        return False
