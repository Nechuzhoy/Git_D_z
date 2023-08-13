nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False,],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, list_list):
        self.list_list = list_list

    def __iter__(self):
        self.index = -1
        self.list_iter = []
        self.list_iter_i = -1
        return self

    def __next__(self):
        self.list_iter_i +=1
        if self.list_iter_i >= len(self.list_iter):
            self.index +=1
            if self.index  >= len(self.list_list) :
                raise StopIteration
            self.list_iter = self.list_list[self.index ]
            self.list_iter_i = 0
        return self.list_iter[self.list_iter_i ]



if __name__ == '__main__':
 for item in FlatIterator(nested_list):
        print(item)
 flat_list = [item for item in FlatIterator(nested_list)]
 print(flat_list)
