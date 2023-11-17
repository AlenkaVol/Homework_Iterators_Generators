list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter_list = 0
        self.len_list = len(self.list_of_list)
        self.results_list = iter([])
        return self

    def __next__(self):
        try:
            next_item = next(self.results_list)
        except StopIteration:
            if self.counter_list == self.len_list:
                raise StopIteration
            self.results_list = iter(self.list_of_list[self.counter_list])
            self.counter_list += 1
            next_item = next(self.results_list)
        return next_item


# test = FlatIterator(list_of_lists_1)
# for i in test:
#     print(i)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()