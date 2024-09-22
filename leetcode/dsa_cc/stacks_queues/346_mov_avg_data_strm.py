from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        

    def next(self, val: int) -> float:

        # Add the next value to the end of the queue
        self.queue.append(val)

        # Check if the size of the window has exceeded the given limit
        # If it has, remove the first element put in
        if len(self.queue) > self.size:
            self.queue.popleft()
        
        # Calculate the average of the values in the queue now
        mov_avg = sum(self.queue) / len(self.queue)
        
        return mov_avg

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == "__main__":
    size1 = 3
    ans1 = []
    ma1 = MovingAverage(size1)
    ans1.append(ma1.next(1))
    ans1.append(ma1.next(10))
    ans1.append(ma1.next(3))
    ans1.append(ma1.next(5))
    print(f"Answer 1: {ans1}")
