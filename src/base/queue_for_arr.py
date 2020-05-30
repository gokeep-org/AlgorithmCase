class ArrQueue:
    arr = []
    max = 0
    head = 0
    put_index = 0

    def __init__(self, max):
        self.max = max

    def put(self, num):
        self.check_queue_len()
        self.arr.append(num)
        self.put_index = self.put_index + 1

    def fetch(self):
        if self.is_empty():
            raise Exception("队列为空")
        else:
            if self.head > self.put_index:
                raise Exception("已经没有元素可以获取了啊")
            res = self.arr[self.head]
            self.head = self.head + 1
            return res

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

    def check_queue_len(self):
        if self.put_index > self.max - 1:
            raise Exception("队列超过最大长度")
        else:
            pass

    def print(self):
        print("head : ", self.head, ",put_index: ", self.put_index, ",arr: " + str(self.arr))


if __name__ == '__main__':
    queue = ArrQueue(3)
    queue.put(1)
    print(queue.fetch())
    queue.print()
    queue.put(2)
    queue.print()

