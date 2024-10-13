from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = nums
        # Create a min heap
        if self.scores:
            heapq.heapify(self.scores)


    def add(self, val: int) -> int:

        # Handle the edge case where the nums array is empty
        if self.scores:
            heapq.heappush(self.scores, val)
        else:
            self.scores = [val]
            return self.scores[0]

        # Ensure min heap is no more than k elements long
        while len(self.scores) > self.k:
            heapq.heappop(self.scores)

        # Return the first element of the heap which, if the heap is k elements long,
        # Will always be the kth largest element
        return self.scores[0]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    # nums1 = [4, 5, 8, 2]
    # k1 = 3
    # obj1 = KthLargest(k1, nums1)
    # print(obj1.add(3))
    # print(obj1.add(5))
    # print(obj1.add(10))
    # print(obj1.add(9))
    # print(obj1.add(4))

    nums2 = []
    k2 = 1
    obj2 = KthLargest(k2, nums2)
    print(obj2.add(-3))
    print(obj2.add(-2))
    print(obj2.add(-4))
    print(obj2.add(0))
    print(obj2.add(4))

