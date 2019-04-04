class Solution:
    def permuteUnique(self, nums):
        counts = self.get_count(nums)
        ret = []
        self.recur(counts, [], ret)
        return ret

    def get_count(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        return counts

    def recur(self, counts, mem, ret):
        if len(counts) == 0:
            ret.append(mem[:])
            print("output: ", mem[:])
            return
        keys = list(counts.keys())
        for key in keys:
            tot_count = counts[key]
            if len(mem) > 0 and mem[-1] == key:
                continue
            for count in range(1, tot_count + 1):
                mem.append(key)
                counts[key] -= 1
                if counts[key] == 0:
                    del counts[key]
                print("picked %d `%d`" % (count, key), "counts = ", counts)
                self.recur(counts, mem, ret)
            counts[key] = tot_count
            for i in range(tot_count):
                mem.pop()
        return


if __name__ == '__main__':
    ipt = [1, 1, 2]
    print("answer: ", Solution().permuteUnique(ipt))
