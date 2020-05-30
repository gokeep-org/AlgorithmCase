class LinkedList:
    element = None
    next = None

    def add(self, num):
        temp = self
        while True:
            if temp.next is None:
                temp.next = LinkedList()
                temp.element = num
                break
            else:
                temp = temp.next
        pass

    def delete(self, index):
        # fir = self.get(index - 1)
        # lat = self.get(index + 1)
        # fir.next = lat
        temp = self
        temp_index = 0
        fir = None
        while True:
            if not temp.next:
                raise Exception("未找到元素节点")
            if index == temp_index:
                las = temp.next
                break
            else:
                fir = temp
                temp = temp.next
                temp_index = temp_index + 1
        fir.next = las

    def get(self, index):
        temp = self
        temp_index = 0
        while True:
            if not temp.next:
                raise Exception("未找到元素节点")
            if index == temp_index:
                return temp
            else:
                temp = temp.next
                temp_index = temp_index + 1

    def update(self, index, new_num):
        element_link = self.get(index)
        element_link.element = new_num

    def list(self):
        temp = self
        index = 0
        while True:
            if temp.next is None:
                break
            else:
                print("index: ", index, ", element： ", temp.element)
                index = index + 1
                temp = temp.next

    def len(self):
        size = 0
        temp = self
        while True:
            if temp.next is None:
                break
            else:
                temp = temp.next
                size = size + 1
        return size


if __name__ == '__main__':
    link = LinkedList()
    print("---------add")
    link.list()
    link.add(1)
    link.add(2)
    link.add(3)
    link.add(4)
    link.list()
    print("----------update")
    link.update(3, 9)
    link.list()
    print("----------len")
    print(link.len())
    print("----------delete")
    link.delete(2)
    link.list()
# print("aaa")
